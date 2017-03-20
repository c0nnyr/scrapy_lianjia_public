# -*- coding: utf-8 -*-

import scrapy, json, re, math
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http import Request, HtmlResponse

import items
class CommunitySpider(scrapy.Spider):
	name = 'community'
	allowed_domains = ['cd.lianjia.com']

	RESBLOCK_URL = 'http://cd.lianjia.com/ershoufang/{page}c{rid}/'
	HOURSE_STATE_URL = 'http://cd.lianjia.com/ershoufang/housestat?hid={hid}&rid={rid}'

	COMMUNITY_ITEM_INFO_RE = r'''require\(\['ershoufang/sellList/index'\],\s*?function\s*?\(main\)\s*?\{\s*?main\((?P<extract>(\s|\S)*?)\);\s*?\}\);'''
	HOUSE_ITEM_INFO_RE = r'''require\(\['ershoufang/sellDetail/detailV3'\],\s*?function\s*?\(init\)\s*?\{\s*init\((?P<extract>(\s|\S)*?)\);\s*?\}\);'''#放在最后的script里面的

	HOUSE_ITEM_COUNT_PER_PAGE = 30

	def __init__(self, rid=None):
		rid = 1611041529992#望江嘉园
		#rid = 3011056075583
		super(CommunitySpider, self).__init__()
		self.start_urls = (self.RESBLOCK_URL.format(rid=rid, page=''), )
		self.rid = rid

	def parse(self, response):
		#parse初始的url,返回小区的信息
		def handle_community(self=self, response=response):
			print 'parsing community', response.url
			search_result = re.search(self.COMMUNITY_ITEM_INFO_RE, response.body)
			if not search_result:
				print 'cj==>cannot succesfully extract community item in start url'
				return
			dct = self._handle_js_object(search_result.group('extract'))

			community = items.CommunityItem()
			community.set_basic_data(dct)
			community.set_url(response.url)

			return community

		community_item = handle_community()
		if not community_item:
			return
		yield community_item

		def handle_house(self=self, response=response):
			house_url_xpath = '/html/body/div[4]/div[1]/ul/li/div[1]/div[1]/a/@href'
			for url in response.xpath(house_url_xpath).extract():
				yield Request(url=url, callback=self.parse_house)
				hid = re.search(r'\d+', url).group(0)
				yield Request(url=self.HOURSE_STATE_URL.format(rid=self.rid, hid=hid), callback=self.parse_house_state, meta={'hid':hid})

		for item in handle_house():
			yield item

		def handle_continue_community(self=self, response=response):
			if not response.meta.get('is_not_first_parse'):
				count = float(community_item.house_count_on_sale)
				page_count = int(math.ceil(count / self.HOUSE_ITEM_COUNT_PER_PAGE))
				for page in xrange(2, page_count + 1):
					yield Request(url=self.RESBLOCK_URL.format(rid=self.rid, page='pg%d' % page), meta={'is_not_first_parse':True})
		for r in handle_continue_community():
			yield r


	def parse_house(self, response):
		print 'parsing house', response.url
		search_result = re.search(self.HOUSE_ITEM_INFO_RE, response.body)
		if not search_result:
			print 'cj==>cannot succesfully extract house item'
			return
		dct = self._handle_js_object(search_result.group('extract'))
		house = items.HouseItem()
		house.set_basic_data(dct)
		house.set_url(response.url)
		return house

	def parse_house_state(self, response):
		print 'parsing house state', response.url
		hid = response.meta['hid']
		dct = json.loads(response.body)
		dct['id'] = hid
		dct['see_count'] = dct['data']['seeRecord']['totalCnt']
		state = items.HouseStateItem()
		state.set_basic_data(dct)
		state.set_url(response.url)
		return state

	@staticmethod
	def _handle_js_object(s):
		pattern = r'^(\s*?)(\w*?)\s*(:)'#添加""
		s = re.sub(pattern, r'\1"\2"\3', s, flags=re.M)#多行模式
		s = s.replace("'", '"')
		return json.loads(s)


