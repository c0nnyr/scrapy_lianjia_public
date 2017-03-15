# -*- coding: utf-8 -*-

import scrapy

from lianjia.items import CommunityItem

class CommunitySpider(scrapy.Spider):
    name = 'community'
    allowed_domains = ['cd.lianjia.com']
    start_urls = [
        'http://cd.lianjia.com/ershoufang/c1611041529992/',
    ]


    ITEM_XPATH = '/html/body/div[4]/div[1]/ul/li'

    TITLE_XPATH = 'div[1]/div[1]/a/text()'
    TOTAL_PRICE_XPATH = 'div[1]/div[6]/div[1]/span/text()'
    PRICE_PER_M_XPATH = 'div[1]/div[6]/div[2]/span/text()'
    LINK_XPATH = 'div[1]/div[1]/a/@href'

    XPATH_ATTR_PAIRS = (
        (TITLE_XPATH, 'title'),
        (TOTAL_PRICE_XPATH, 'total_price'),
        (PRICE_PER_M_XPATH, 'price_per_m'),
        (LINK_XPATH, 'link'),
    )

    def parse(self, response):
        for community_item in response.xpath(self.ITEM_XPATH):
            item = CommunityItem()
            for xpath, attr in self.XPATH_ATTR_PAIRS:
                tmp = community_item.xpath(xpath).extract()
                item[attr] = tmp[0] if tmp else None
            print item.__dict__
            yield item
