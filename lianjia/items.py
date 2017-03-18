# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class LianJiaItem(scrapy.Item):
    url = scrapy.Field()
    FILTER_DATA_MAP = {
        #lianjia_item, house_item
    }
    original_data = scrapy.Field()

    def set_basic_data(self, dct):
        for k, v in dct.iteritems():
            if k in self.FILTER_DATA_MAP:
                self[self.FILTER_DATA_MAP[k]] = v
        self['original_data'] = dct.copy()

    def set_url(self, url):
        self['url'] = url

class CommunityItem(LianJiaItem):
    resblock_id = scrapy.Field()
    house_count_on_sale = scrapy.Field()
    house_ids_on_sale = scrapy.Field()
    uuid = scrapy.Field()

    FILTER_DATA_MAP = {
        #lianjia_item, house_item
        'cid':'resblock_id',
        'count':'house_count_on_sale',
        'ids':'house_ids_on_sale',
        'uuid':'uuid',
    }

class HouseItem(LianJiaItem):
    house_type = scrapy.Field()
    house_size = scrapy.Field()
    register_time = scrapy.Field()
    total_price = scrapy.Field()
    price = scrapy.Field()
    house_id = scrapy.Field()
    resblock_id = scrapy.Field()
    resblock_name = scrapy.Field()
    is_removed = scrapy.Field()
    resblock_position = scrapy.Field()
    city_id = scrapy.Field()
    title = scrapy.Field()
    uuid = scrapy.Field()

    FILTER_DATA_MAP = {
        #lianjia_item, house_item
        'houseType':'house_type',
        'area':'house_size',
        'registerTime':'register_time',
        'totalPrice':'total_price',
        'price':'price',
        'houseId':'house_id',
        'resblockId':'resblock_id',
        'resblockName':'resblock_name',
        'isRemove':'is_removed',
        'resblockPosition':'resblock_position',
        'cityId':'city_id',
        'uuid':'uuid',
        'title':'title',
    }

