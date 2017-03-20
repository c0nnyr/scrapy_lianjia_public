# -*- coding: utf-8 -*-

import scrapy, json, re, math
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http import Request, HtmlResponse

class AllCommunitySpider(scrapy.Spider):
	name = 'all_community'
	allowed_domains = ['cd.lianjia.com']

	start_urls = (
		'http://cd.lianjia.com/xiaoqu/',
	)

	def parse(self, response):
		#第0阶段就这这里，爬取start_urls的结果

		#meta = response.meta
		#if meta.get('is_first_parse'):

		def _handle(self=self, response=response):
			community_xpath = '/html/body/div[4]/div[1]/ul/li[1]'
			pack = lambda xpath, re_filter=None, default=None:(xpath, re_filter, default)
			community_attr_map = {
				#attr xpath, re_filter
				'link':pack('div[2]/div[2]/a/@href',),
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
				print 'parsing item', community_item
				yield community_item

		return _handle()



