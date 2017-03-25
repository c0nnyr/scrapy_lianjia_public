# -*- coding: utf-8 -*-

import scrapy, json, re, math
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http import Request, HtmlResponse
from base_spider import BaseSpider, check_validate

import items
class CommunitySpider(BaseSpider):
	name = 'community'

	RESBLOCK_URL = 'http://cd.lianjia.com/ershoufang/{page}c{rid}/'
	HOURSE_STATE_URL = 'http://cd.lianjia.com/ershoufang/housestat?hid={hid}&rid={rid}'

	COMMUNITY_ITEM_INFO_RE = r'''require\(\['ershoufang/sellList/index'\],\s*?function\s*?\(main\)\s*?\{\s*?main\((?P<(\s|\S)*?)\);\s*?\}\);'''
	HOUSE_ITEM_INFO_RE = r'''require\(\['ershoufang/sellDetail/detailV3'\],\s*?function\s*?\(init\)\s*?\{\s*init\((?P<extract>(\s|\S)*?)\);\s*?\}\);'''#放在最后的script里面的

	HOUSE_ITEM_COUNT_PER_PAGE = 30

	def __init__(self, rid=None):
		rid = 1611041529992#望江嘉园
		#rid = 3011056075583
		super(CommunitySpider, self).__init__()
		self.start_urls = (self.RESBLOCK_URL.format(rid=rid, page=''), )
		self.rid = rid

	@check_validate
	def parse(self, response):
		#parse初始的url,返回小区的信息
		start_url = response.meta.get('start_url', response.url)
		print 'parsing community', response.url
		search_result = re.search(self.COMMUNITY_ITEM_INFO_RE, response.body)
		if not search_result:
			print 'cj==>cannot succesfully extract community item in start url'
			return
		dct = self._handle_js_object(search_result.group('extract'))

		community_item = items.CommunityItem(
			house_count_on_sale=dct['count'],
			house_ids_on_sale=dct['ids'],
			uuid=dct['uuid'],

			id=dct['cid'],
			start_url=start_url,
			url=response.url,
			original_data=str(dct),
		)
		if not community_item:
			return
		yield community_item

		##################
		house_url_xpath = '/html/body/div[4]/div[1]/ul/li/div[1]/div[1]/a/@href'
		for url in response.xpath(house_url_xpath).extract():
			hid = re.search(r'\d+', url).group(0)
			yield Request(url=url, callback=self.parse_house_1, meta={'hid':hid, 'start_url':start_url})
			yield Request(url=self.HOURSE_STATE_URL.format(rid=self.rid, hid=hid), callback=self.parse_house_state_1, meta={'hid':hid, 'start_url':start_url})

		##################
		if not response.meta.get('page'):
			count = float(community_item.house_count_on_sale)
			page_count = int(math.ceil(count / self.HOUSE_ITEM_COUNT_PER_PAGE))
			for page in xrange(2, page_count + 1):
				yield Request(url=self.RESBLOCK_URL.format(rid=self.rid, page='pg%d' % page), meta={'page':page, 'start_url':start_url})

	def parse_house_1(self, response):
		print 'parsing house', response.url
		search_result = re.search(self.HOUSE_ITEM_INFO_RE, response.body)
		if not search_result:
			print 'cj==>cannot succesfully extract house item'
			return
		dct = self._handle_js_object(search_result.group('extract'))
		return items.HouseItem(
			house_type=dct['houseType'],
			house_size=dct['area'],
			register_time=dct['registerTime'],
			total_price=dct['totalPrice'],
			price=dct['price'],
			resblock_id=dct['resblockId'],
			resblock_name=dct['resblockName'],
			is_removed=dct['isRemove'],
			resblock_position=dct['resblockPosition'],
			city_id=dct['cityId'],
			uuid=dct['uuid'],
			title=dct['title'],

			id=dct['houseId'],
			url=response.url,
			original_data=str(dct),
			start_url=response.meta.get('start_url'),
		)

	def parse_house_state_1(self, response):
		print 'parsing house state', response.url
		hid = response.meta['hid']
		dct = json.loads(response.body)
		dct['id'] = hid
		dct['see_count'] = dct['data']['seeRecord']['totalCnt']
		return items.HouseStateItem(
			see_count=dct['see_count'],

			id=dct['id'],
			url=response.url,
			original_data=str(dct),
			start_url=response.meta.get('start_url'),
		)

	@staticmethod
	def _handle_js_object(s):
		pattern = r'^(\s*?)(\w*?)\s*(:)'#添加""
		s = re.sub(pattern, r'\1"\2"\3', s, flags=re.M)#多行模式
		s = s.replace("'", '"')
		return json.loads(s)


