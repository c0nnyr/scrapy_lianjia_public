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
    url = Column(Text())
    original_data = Column(Text())
    date = Column(Text(), primary_key=True)
    id = Column(Integer(), primary_key=True)

    def __init__(self, **kwargs):
        super(LianJiaItem, self).__init__()
        self.date = self.get_today_str()

    def init(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    @staticmethod
    def get_today_str():
        return datetime.date.today().strftime('%y-%m-%d')

class CommunityItem(Model, LianJiaItem):
    __tablename__ = 'community'

    house_count_on_sale = Column(Integer())
    house_ids_on_sale = Column(Text())
    uuid = Column(Text())

    def __init__(self, **kwargs):
        Model.__init__(self)
        LianJiaItem.__init__(self, **kwargs)


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

    def __init__(self, **kwargs):
        Model.__init__(self)
        LianJiaItem.__init__(self, **kwargs)

class HouseStateItem(Model, LianJiaItem):
    __tablename__ = 'house_state'
    see_count = Column(Integer())

    def __init__(self, **kwargs):
        Model.__init__(self)
        LianJiaItem.__init__(self, **kwargs)

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

    def __init__(self, **kwargs):
        Model.__init__(self)
        LianJiaItem.__init__(self, **kwargs)
