# -*- coding: utf-8 -*-

import scrapy, json, re, math
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http import Request, HtmlResponse

import items, base_spider

class CommunityDealSpider(base_spider.BaseSpider):
	name = 'deal_community'
	allowed_domains = ['cd.lianjia.com']

	COMMUNITY_DEAL_URL = 'http://cd.lianjia.com/chengjiao/{page}c%s/'

	def __init__(self, rid):
		super(CommunityDealSpider, self).__init__()
		#self.rid = 1611041529992
		self.rid = rid# or 1611041529992#望江嘉园
		self.start_urls = (
			self.COMMUNITY_DEAL_URL.format(page='') % self.rid,
		)

	def parse(self, response):
		#第0阶段就这这里，爬取start_urls的结果

		item_xpath = '/html/body/div[4]/div[1]/ul/li'
		attr_map = {
			#attr xpath, re_filter
			#'link':pack('div[2]/div[2]/a/@href',),#这里不能再添加根了，不能/divxx or /li/div
			'id':self.pack('div/div[1]/a/@href', r'(?P<extract>\d+)'),
			'url':self.pack('div/div[1]/a/@href', ),
			'title':self.pack('div/div[1]/a/text()',),
			'date':self.pack('div/div[2]/div[2]/text()',),
			'total_price':self.pack('div/div[2]/div[3]/span/text()',),
			'price_per_sm':self.pack('div/div[3]/div[3]/span/text()',),
			'deal_by':self.pack('div/div[3]/div[2]/text()',),
			'description':self.pack('div/div[2]/div[1]/text()',),
			'description2':self.pack('div/div[3]/div[1]/text()',),
			'district_description':self.pack('div/div[4]/span[2]/span/text()',),
			'price_when_on':self.pack('div/div[5]/span[2]/span[1]/text()', r'(?P<extract>\d+)'),
			'days_when_sale':self.pack('div/div[5]/span[2]/span[2]/text()', r'(?P<extract>\d+)'),
		}

		for item in self._parse_items(response, item_xpath, attr_map, items.DealItem, self.add_page):
			if items.DealItem.is_already_crawled(item.id, item.date):
				print 'already crawled, stop now', item.id, item.date
				return
			yield item

		'/html/body/div[3]/div[1]/div[2]/div[1]/span'
		for r in self._parse_pages(response, self.COMMUNITY_DEAL_URL % self.rid, '/html/body/div[4]/div[1]/div[2]/div[1]/span/text()', 30, items.DealItem):
			#这里虽然提供了一个总小区个数,但是只提供了100页可以浏览....
			yield r

