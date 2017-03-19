# -*- coding: utf-8 -*-

import scrapy, json, re, math
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http import Request, HtmlResponse

from lianjia import items
class CommunitySpider(CrawlSpider):
    name = 'community'
    allowed_domains = ['cd.lianjia.com']

    RESBLOCK_URL = 'http://cd.lianjia.com/ershoufang/{page}c{rid}/'
    HOURSE_STATE_URL = 'http://cd.lianjia.com/ershoufang/housestat?hid={hid}&rid={rid}'

    rules = (
        Rule(LinkExtractor(restrict_xpaths='/html/body/div[4]/div[1]/ul/li/div[1]/div[1]/a'), callback='parse_house_item'),
    )

    COMMUNITY_ITEM_INFO_RE = r'''require\(\['ershoufang/sellList/index'\],\s*?function\s*?\(main\)\s*?\{\s*?main\((?P<extract>(\s|\S)*?)\);\s*?\}\);'''
    HOUSE_ITEM_INFO_RE = r'''require\(\['ershoufang/sellDetail/detailV3'\],\s*?function\s*?\(init\)\s*?\{\s*init\((?P<extract>(\s|\S)*?)\);\s*?\}\);'''#放在最后的script里面的

    HOUSE_ITEM_COUNT_PER_PAGE = 30

    def __init__(self, rid=None):
        rid = 1611041529992#望江嘉园
        #rid = 3011056075583
        self.start_urls = (self.RESBLOCK_URL.format(rid=rid, page=''), )
        super(CommunitySpider, self).__init__()
        self.rid = rid

    def parse_start_url(self, response):
        #parse初始的url,返回小区的信息
        community_item = self._parse_community(response)
        yield community_item
        if not community_item:
            return
        count = int(community_item.house_count_on_sale)
        page_count = int(math.ceil(float(count) / self.HOUSE_ITEM_COUNT_PER_PAGE))
        for page in xrange(2, page_count + 1):
            r = Request(url=self.RESBLOCK_URL.format(rid=self.rid, page='pg%d' % page), callback=self.parse_dynamic_start_url)
            yield r

    def parse_dynamic_start_url(self, response):
        return self._parse_response(response, self._parse_community, {}, True)

    def _parse_community(self, response):
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

    def parse_house_item(self, response):
        print 'parsing house', response.url
        search_result = re.search(self.HOUSE_ITEM_INFO_RE, response.body)
        if not search_result:
            print 'cj==>cannot succesfully extract house item'
            return
        dct = self._handle_js_object(search_result.group('extract'))

        house = items.HouseItem()
        house.set_basic_data(dct)
        house.set_url(response.url)

        yield house

        r = Request(url=self.HOURSE_STATE_URL.format(rid=self.rid, hid=house.id), \
                    callback=lambda response:self.parse_house_state(response, house.id))
        yield r

    def parse_house_state(self, response, hid):
        return self._parse_response(response, lambda response:self._parse_house_state_item(response, hid), {}, False)

    def _parse_house_state_item(self, response, hid):
        print 'parsing house state', response.url
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


