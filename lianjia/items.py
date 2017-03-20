# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime, os
from sqlalchemy import Column, Integer, String, Text, Float, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Model = declarative_base(name='Model')

class LianJiaItem(dict):
    scrapy_time = scrapy.Field()

    url = Column(Text())
    original_data = Column(Text())
    date = Column(Text(), primary_key=True)
    id = Column(Integer(), primary_key=True)

    FILTER_DATA_MAP = {
        #lianjia_item, house_item
    }

    def __init__(self):
        super(LianJiaItem, self).__init__()
        self.date = self.get_today_str()
        self['scrapy_time'] = self.date

    @staticmethod
    def get_today_str():
        return datetime.date.today().strftime('%y-%m-%d')

    def set_basic_data(self, dct):
        for k, v in dct.iteritems():
            if k in self.FILTER_DATA_MAP:
                setattr(self, self.FILTER_DATA_MAP[k], v)
        self.original_data = str(dct)

    def set_url(self, url):
        self.url = url

class CommunityItem(Model, LianJiaItem):
    __tablename__ = 'community'
    house_count_on_sale = Column(Integer())
    house_ids_on_sale = Column(Text())
    uuid = Column(Text())

    FILTER_DATA_MAP = {
        #lianjia_item, house_item
        'cid':'id',
        'count':'house_count_on_sale',
        'ids':'house_ids_on_sale',
        'uuid':'uuid',
    }

    def __init__(self):
        Model.__init__(self)
        LianJiaItem.__init__(self)

class HouseItem(Model, LianJiaItem):
    __tablename__ = 'house'

    house_type = Column(Text())
    house_size = Column(Float())
    register_time = Column(Text())
    total_price = Column(Integer())
    price = Column(Float())
    id = Column(Integer(), primary_key=True)
    resblock_id = Column(Integer())
    resblock_name = Column(Text())
    is_removed = Column(Integer())
    resblock_position = Column(Text())
    city_id = Column(Integer())
    title = Column(Text())
    uuid = Column(Text())

    FILTER_DATA_MAP = {
        #lianjia_item, house_item
        'houseType':'house_type',
        'area':'house_size',
        'registerTime':'register_time',
        'totalPrice':'total_price',
        'price':'price',
        'houseId':'id',
        'resblockId':'resblock_id',
        'resblockName':'resblock_name',
        'isRemove':'is_removed',
        'resblockPosition':'resblock_position',
        'cityId':'city_id',
        'uuid':'uuid',
        'title':'title',
    }

    def __init__(self):
        Model.__init__(self)
        LianJiaItem.__init__(self)

class HouseStateItem(Model, LianJiaItem):
    __tablename__ = 'house_state'

    see_count = Column(Integer())

    FILTER_DATA_MAP = {
        #lianjia_item, house_item
        'id':'id',
        'see_count':'see_count',
    }

    def __init__(self):
        Model.__init__(self)
        LianJiaItem.__init__(self)


class OriginalCommunityItem(Model, LianJiaItem):
    __tablename__ = 'original_community'
    title = Column(Text())
    count_on_sale = Column(Integer())
    price_per_sm = Column(Float())
    count_on_rent = Column(Integer())
    count_sold_90days = Column(Integer())
    district = Column(Text())
    bizcircle = Column(Text())
    year_built = Column(Integer())

    FILTER_DATA_MAP = {
        #lianjia_item, house_item
        'id':'id',
        'title':'title',
        'count_on_sale':'count_on_sale',
        'price_per_sm':'price_per_sm',
        'count_on_rent':'count_on_rent',
        'count_sold_90days':'count_sold_90days',
        'district':'district',
        'bizcircle':'bizcircle',
        'year_built':'year_built',
    }

    def __init__(self):
        Model.__init__(self)
        LianJiaItem.__init__(self)

