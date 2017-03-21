# -*- coding: utf-8 -*-

import scrapy, json, re, math
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http import Request, HtmlResponse

import items

class CommunityDealSpider(scrapy.Spider):
	name = 'all_community'
	allowed_domains = ['cd.lianjia.com']

	COMMUNITY_DEAL_URL = 'http://cd.lianjia.com/chengjiao/{page}c{rid}/'

	def __init__(self, rid=None):
		super(CommunityDealSpider, self).__init__()
		rid = 1611041529992#望江嘉园
		self.start_urls = (
			self.COMMUNITY_DEAL_URL.format(page='', rid=rid),
		)

	def parse(self, response):
		#第0阶段就这这里，爬取start_urls的结果

		def handle(self=self, response=response):
			house_xpath = '/html/body/div[4]/div[1]/ul/li'
			pack = lambda xpath, re_filter=None, default=None:(xpath, re_filter, default)#这个辅助解包用好
			house_attr_map = {
				#attr xpath, re_filter
				#'link':pack('div[2]/div[2]/a/@href',),#这里不能再添加根了，不能/divxx or /li/div
				'id':pack('div/div[1]/a/@href', r'(?P<extract>\d+)'),
				'title':pack('div/div[1]/a/text()',),
				'date':pack('div/div[2]/div[2]/text()',),
				'total_price':pack('div/div[2]/div[3]/span/text()',),
				'price_per_sm':pack('div/div[3]/div[3]/span/text()',),
				'deal_by':pack('div/div[3]/div[2]/text()',),
				'description':pack('div/div[2]/div[1]/text()',),
				'description2':pack('div/div[3]/div[1]/text()',),
				'district_description':pack('div/div[4]/span[2]/span/text()',),
				'price_when_on':pack('div/div[5]/span[2]/span[1]/text()', r'(?P<extract>\d+)'),
				'days_when_sale':pack('div/div[5]/span[2]/span[2]/text()', r'(?P<extract>\d+)'),
			}

			#正式开始解析
			house_sel_items = response.xpath(house_xpath)
			for sel in house_sel_items:
				dct = {}
				for attr, item in house_attr_map.iteritems():
					xpath, re_filter, default = item
					content = ''.join(sel.xpath(xpath).extract())#对于year_built，有多项
					if re_filter:
						try:
							content = re.search(re_filter, content).group('extract')
						except:
							content = default
					dct[attr] = content
				yield items.DealItem(
					title = dct['title'],
					date = dct['date'],
					total_price = dct['total_price'],
					price_per_sm = dct['price_per_sm'],
					deal_by = dct['deal_by'],
					description = dct['description'],
					description2 = dct['description2'],
					district_description = dct['district_description'],
					price_when_on = dct['price_when_on'],
					days_when_sale = dct['days_when_sale'],

					id=dct['id'],
					url=response.url,
					original_data=str(dct),
				)

		for item in handle():
			yield item

		meta = response.meta
		if not meta.get('is_not_first_parse'):
			DEAL_COUNT_PER_PAGE = 30
			total_count_xpath = '/html/body/div[4]/div[1]/div[2]/div[1]/span/text()'
			total_count = float(response.xpath(total_count_xpath).extract_first())
			total_pages = int(math.ceil(total_count / DEAL_COUNT_PER_PAGE))
			for page in xrange(2, total_pages + 1):
				url = self.COMMUNITY_DEAL_URL.format(page='pg%s' % page)
				if items.DealItem.check_page_crawled(url, DEAL_COUNT_PER_PAGE):
					print 'has crawled already', url
					continue
				yield Request(url, meta={'is_not_first_parse':True})
