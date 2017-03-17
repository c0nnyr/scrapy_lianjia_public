# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class HouseItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    total_price = scrapy.Field()
    price_per_m = scrapy.Field()
    cityId = scrapy.Field()

    def __init__(self, dct):
        super(HouseItem, self).__init__((k, v) for k, v in dct.iteritems() if k in self.fields)
