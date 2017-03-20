# -*- coding: utf-8 -*-

import scrapy, json, re, math
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http import Request, HtmlResponse

import items

class AllCommunitySpider(scrapy.Spider):
	name = 'all_community'
	allowed_domains = ['cd.lianjia.com']

	COMMUNITY_URL = 'http://cd.lianjia.com/xiaoqu/{}'
	start_urls = (
		COMMUNITY_URL.format(''),
	)

	def parse(self, response):
		#第0阶段就这这里，爬取start_urls的结果

		def _handle(self=self, response=response):
			community_xpath = '/html/body/div[4]/div[1]/ul/li'
			pack = lambda xpath, re_filter=None, default=None:(xpath, re_filter, default)#这个辅助解包用好
			community_attr_map = {
				#attr xpath, re_filter
				#'link':pack('div[2]/div[2]/a/@href',),#这里不能再添加根了，不能/divxx or /li/div
				'id':pack('div[2]/div[2]/a/@href', r'(?P<extract>\d+)'),
				'title':pack('div[1]/div[1]/a/text()',),
				'count_on_sale':pack('div[2]/div[2]/a/span/text()',),
				'price_per_sm':pack('div[2]/div[1]/div[1]/span/text()',),
				'count_on_rent':pack('div[1]/div[2]/a[2]/text()', r'(?P<extract>\d+)'),
				'count_sold_90days':pack('div[1]/div[2]/a[1]/text()', r'90\S+(?P<extract>\d+)'),
				'district':pack('div[1]/div[3]/a[1]/text()',),
				'bizcircle':pack('div[1]/div[3]/a[2]/text()',),
				'year_built':pack('div[1]/div[3]/text()',  r'(?P<extract>\d+)', '0'),
			}

			#正式开始解析
			community_sel_items = response.xpath(community_xpath)
			for sel in community_sel_items:
				community_item = {}
				for attr, item in community_attr_map.iteritems():
					xpath, re_filter, default = item
					content = ''.join(sel.xpath(xpath).extract())#对于year_built，有多项
					if re_filter:
						try:
							content = re.search(re_filter, content).group('extract')
						except:
							content = default
					community_item[attr] = content
				original_community_item = items.OriginalCommunityItem()
				original_community_item.set_basic_data(community_item)
				original_community_item.set_url(response.url)
				yield original_community_item

		for item in _handle():
			yield item

		meta = response.meta
		if not meta.get('is_not_first_parse'):
			COMMUNITY_COUNT_PER_PAGE = 30
			total_count_xpath = '/html/body/div[4]/div[1]/div[2]/h2/span/text()'
			total_count = float(response.xpath(total_count_xpath).extract_first())
			total_pages = int(math.ceil(total_count / COMMUNITY_COUNT_PER_PAGE))
			for page in xrange(2, total_pages + 1):
				yield Request(self.COMMUNITY_URL.format('pg%s/' % page), meta={'is_not_first_parse':True})
