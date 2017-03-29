# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime, os
from sqlalchemy import Column, Integer, String, Text, Float, create_engine, and_, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import dbhelper as db
Model = declarative_base(name='Model')

class LianJiaItem(dict):
    scrapy_date = scrapy.Field()#必须有一个这个Field,否则就会当做没有item,中断掉
    scrapy_id = scrapy.Field()

    start_url = Column(Text())
    url = Column(Text())
    original_data = Column(Text())
    date = Column(Text(), primary_key=True)
    id = Column(Integer(), primary_key=True)

    def __init__(self, **kwargs):
        super(LianJiaItem, self).__init__()
        assert all((k in kwargs) for k in ('start_url', 'url', 'original_data', 'id')), "must contain keys 'start_url', 'url', 'original_data', 'id'"
        self.date = self.get_today_str()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

        self['scrapy_date'] = self.date
        self['scrapy_id'] = self.id

    @staticmethod
    def get_today_str(delta=0):
        return (datetime.date.today() + datetime.timedelta(delta)).strftime('%y-%m-%d')

    @classmethod
    def check_page_crawled(cls, page, page_count, start_url):
        assert hasattr(cls, 'page'), 'must exist attr page'
        return db.session and db.session.query(cls).filter(and_(cls.start_url==start_url, cls.page==page, cls.date==cls.get_today_str())).count() == page_count

class CommunityItem(LianJiaItem, Model):
    __tablename__ = 'community'

    house_count_on_sale = Column(Integer())
    house_ids_on_sale = Column(Text())
    uuid = Column(Text())

class HouseItem(LianJiaItem, Model):
    __tablename__ = 'house'

    house_type = Column(Text())
    house_size = Column(Float())
    register_time = Column(Text())
    total_price = Column(Integer())
    price = Column(Float())
    resblock_id = Column(Integer())
    resblock_name = Column(Text())
    is_removed = Column(Integer())
    resblock_position = Column(Text())
    city_id = Column(Integer())
    title = Column(Text())
    uuid = Column(Text())

class HouseStateItem(LianJiaItem, Model):
    __tablename__ = 'house_state'
    see_count = Column(Integer())

class OriginalCommunityItem(LianJiaItem, Model):
    __tablename__ = 'original_community'
    title = Column(Text())
    count_on_sale = Column(Integer())
    price_per_sm = Column(Float())
    count_on_rent = Column(Integer())
    count_sold_90days = Column(Integer())
    district = Column(Text())
    bizcircle = Column(Text())
    year_built = Column(Integer())
    page = Column(Integer())

class DealItem(LianJiaItem, Model):
    __tablename__ = 'deal_item'

    title = Column(Text())
    total_price = Column(Text())
    price_per_sm = Column(Text())
    deal_by = Column(Text())
    description = Column(Text())
    description2 = Column(Text())
    district_description = Column(Text())
    price_when_on = Column(Text())
    days_when_sale = Column(Text())
    page = Column(Integer())

    @classmethod
    def is_already_crawled(cls, id, date):
        return db.session and db.session.query(cls).filter(and_(cls.id==id, cls.date==date)).count() == 1

Model.metadata.create_all(db.engine)#类型建立后,才能这样建立表
