# -*- coding: utf-8 -*-

import scrapy, json, re, math
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http import Request, HtmlResponse

import items
import base_spider

class AllCommunitySpider(base_spider.BaseSpider):
	name = 'all_community'
	allowed_domains = ['cd.lianjia.com']

	COMMUNITY_URL = 'http://cd.lianjia.com/xiaoqu/{page}p%s/'
	start_urls = (
		COMMUNITY_URL.format(page='') % 1,#<0.5
		COMMUNITY_URL.format(page='') % 2,#0.5~0.8
		COMMUNITY_URL.format(page='') % 3,#0.8~1
		COMMUNITY_URL.format(page='') % 4,#1~1.5
		COMMUNITY_URL.format(page='') % 5,#1.5~2
		COMMUNITY_URL.format(page='') % 6,#>2
	)

	def parse(self, response):
		#第0阶段就这这里，爬取start_urls的结果
		xpath = '/html/body/div[4]/div[1]/ul/li'
		attr_map = {
			#attr xpath, re_filter
			'url':self.pack('div[2]/div[2]/a/@href',),#这里不能再添加根了，不能/divxx or /li/div
			'id':self.pack('div[2]/div[2]/a/@href', r'(?P<extract>\d+)'),
			'title':self.pack('div[1]/div[1]/a/text()',),
			'count_on_sale':self.pack('div[2]/div[2]/a/span/text()',),
			'price_per_sm':self.pack('div[2]/div[1]/div[1]/span/text()',),
			'count_on_rent':self.pack('div[1]/div[2]/a[2]/text()', r'(?P<extract>\d+)'),
			'count_sold_90days':self.pack('div[1]/div[2]/a[1]/text()', r'90\S+(?P<extract>\d+)'),
			'district':self.pack('div[1]/div[3]/a[1]/text()',),
			'bizcircle':self.pack('div[1]/div[3]/a[2]/text()',),
			'year_built':self.pack('div[1]/div[3]/text()',  r'(?P<extract>\d+)', '0'),
		}

		#正式开始解析
		for item in self._parse_items(response, xpath, attr_map, items.OriginalCommunityItem, self.add_page):
			yield item

		price_level = re.search(r'p(\d)', response.url).group(1)
		for r in self._parse_pages(response, self.COMMUNITY_URL % price_level, '/html/body/div[4]/div[1]/div[2]/h2/span/text()', 30, items.OriginalCommunityItem):
			#这里虽然提供了一个总小区个数,但是只提供了100页可以浏览....
			yield r
