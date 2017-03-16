# -*- coding: utf-8 -*-

import scrapy
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
        'total_price': '/html/body/div[5]/div[2]/div[2]/span[1]/text()',
    }
    def parse_item(self, response):
        print response.body
        house = items.HouseItem()
        for attr, xpath in self.ITEM_XPATH_MAP.iteritems():
            house[attr] = response.xpath(xpath).extract_first()
        return house


