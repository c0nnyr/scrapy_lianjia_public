# -*- coding: utf-8 -*-

import scrapy, json, re, math
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http import Request, HtmlResponse

import items

class BaseSpider(scrapy.Spider):
    name = 'must_change_this_name'

    @staticmethod
    def pack(xpath, re_filter=None, default=0):
        return xpath, re_filter, default#这个辅助解包用好

    def _parse_items(self, response, item_xpath, attr_map, item_cls, dct_handler=None):
        sel_items = response.xpath(item_xpath)
        for sel in sel_items:
            dct = {}
            for attr, item in attr_map.iteritems():
                xpath, re_filter, default = item
                content = ''.join(sel.xpath(xpath).extract())#对于year_built，有多项
                if re_filter:
                    try:
                        content = re.search(re_filter, content).group('extract')
                    except:
                        content = default
                dct[attr] = content
            if dct_handler:
                dct = dct_handler(response, dct)
            dct['start_url'] = response.meta.get('start_url', response.url)
            dct['original_data'] = str(dct)
            yield item_cls(**dct)

    def _parse_pages(self, response, url_template, total_count_xpath, count_per_page, item_cls):
        meta = response.meta
        if not meta.get('page'):
            total_count = int(response.xpath(total_count_xpath).extract_first())
            total_pages = min(int(math.ceil(float(total_count) / count_per_page)), 100) if total_count != 0 else 0#最多允许爬去100页
            print 'find total pages', total_pages
            for page in xrange(2, total_pages + 1):
                url = url_template.format(page='pg%s' % page)
                start_url = url_template.format(page='')
                if item_cls.check_page_crawled(page, count_per_page, start_url=start_url):
                    print 'has crawled already', url
                    continue
                print 'requesting url', url
                yield Request(url, meta={'page':page, 'start_url':start_url})

    @staticmethod
    def add_page(response, dct):
        dct['page'] = response.meta.get('page', 1)
        return dct

