# -*- coding: utf-8 -*-

import scrapy, json, re
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from lianjia import items

class CommunitySpider(CrawlSpider):
    name = 'community'
    allowed_domains = ['cd.lianjia.com']
    start_urls = [
        'http://cd.lianjia.com/ershoufang/c1611041529992/',
    ]

    rules = (
        Rule(LinkExtractor(restrict_xpaths='/html/body/div[4]/div[1]/ul/li[1]/div[1]/div[1]/a'), callback='parse_item', process_links='process_links'),
    )

    ITEM_XPATH_MAP = {
        #attr, xpath
        #'total_price': '/html/body/div[5]/div[2]/div[2]/span[1]/text()',
    }

    HOUSE_ITEM_INFO_RE = r'''require\(\['ershoufang/sellDetail/detailV3'\],function\(init\)\{\s*init\((?P<extract>(\s|\S)*?)\);\s*\}\);'''#放在最后的script里面的

    def pcess_links(self, links):
        return (links[0], ) if links else ()

    def parse_item(self, response):
        content = response.xpath(self.HOUSE_ITEM_INFO_RE).extract()
        dct = self._handle_js_object(content)
        house = items.HouseItem(dct)
        print house.__dict__

        #其他的一些信息
        for attr, xpath in self.ITEM_XPATH_MAP.iteritems():
            house[attr] = response.xpath(xpath).extract_first()

        return house

    @staticmethod
    def _handle_js_object(s):
        pattern = r'^(\s*?)(\w*?)(:)'#添加""
        s = re.sub(pattern, r'\1"\2"\3', s, flags=re.M)#多行模式
        s = s.replace("'", '"')
        return json.loads(s)


