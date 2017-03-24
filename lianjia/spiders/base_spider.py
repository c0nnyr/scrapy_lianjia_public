# -*- coding: utf-8 -*-

import scrapy, json, re, math
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http import Request, HtmlResponse

import items, functools, types

def check_validate(func):
	@functools.wraps(func)
	def _func(self, response):
		need_validate = False
		for r in self.try_validate(response):
			need_validate = True
			yield r
		if not need_validate:
			ret = func(self, response)
			if isinstance(ret, types.GeneratorType):
				for r in ret:
					yield r
			else:
				yield ret
	return _func

class BaseSpider(scrapy.Spider):
	name = 'must_change_this_name'

	VALIDATE_IMG_URL = 'http://captcha.lianjia.com/human/'

	@staticmethod
	def pack(xpath, re_filter=None, default=0):
		return xpath, re_filter, default#这个辅助解包用好

	def _parse_items(self, response, item_xpath, attr_map, item_cls, dct_handler=None):
		sel_items = response.xpath(item_xpath)
		for sel in sel_items:
			dct = {}
			for attr, item in attr_map.iteritems():
				xpath, re_filter, default = item
				content = ''.join(sel.xpath(xpath).extract())#对于year_built，有多项
				if re_filter:
					try:
						content = re.search(re_filter, content).group('extract')
					except:
						content = default
				dct[attr] = content
			if dct_handler:
				dct = dct_handler(response, dct)
			dct['start_url'] = response.meta.get('start_url', response.url)
			dct['original_data'] = str(dct)
			yield item_cls(**dct)

	def _parse_pages(self, response, url_template, total_count_xpath, count_per_page, item_cls):
		meta = response.meta
		if not meta.get('page'):
			try:
				total_count = int(response.xpath(total_count_xpath).extract_first())
				total_pages = min(int(math.ceil(float(total_count) / count_per_page)), 100)#最多允许爬去100页
			except:
				total_pages = 0
				total_count = 0
			print 'find total pages', total_pages
			for page in xrange(2, total_pages + 1):
				url = url_template.format(page='pg%s' % page)
				start_url = url_template.format(page='')
				if item_cls.check_page_crawled(page, count_per_page, start_url=start_url):
					print 'has crawled already', url
					continue
				print 'requesting url', url
				yield Request(url, meta={'page':page, 'start_url':start_url})

	@staticmethod
	def add_page(response, dct):
		dct['page'] = response.meta.get('page', 1)
		return dct


	def try_validate(self, response):
		if 'captcha.lianjia.com/' not in response.url:
			return
		else:
			csrf_xpath = '/html/body/div/div[2]/div[1]/ul/form/input[3]/@value'#does not work, cannot find form
			csrf = response.xpath(csrf_xpath).extract_first()
			yield Request(self.VALIDATE_IMG_URL, callback=self._parse_validate_imgs, meta={'csrf':csrf})

	def _parse_validate_imgs(self, response):
		print response.body, response.url, response.meta
		pass

