# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import items

#Model = declarative_base(name='Model')
#
#class HouseItemModel(Model):
#    __tablename__ = 'house'
#    id = Column(Integer, primary_key=True)
#
#   # house_type = scrapy.Field()
#   # house_size = scrapy.Field()
#   # register_time = scrapy.Field()
#   # total_price = scrapy.Field()
#    price = Column(Integer)
#    house_id = Column(String(20))
#   # resblock_id = scrapy.Field()
#   # resblock_name = scrapy.Field()
#   # is_removed = scrapy.Field()
#   # resblock_position = scrapy.Field()
#   # city_id = scrapy.Field()
#   # title = scrapy.Field()
#   # uuid = scrapy.Field()
#
#    def __init__(self, item):
#        super(HouseItemModel, self).__init__()
#        self.price = item['price']
#        self.house_id = item['house_id']

class LianjiaPipeline(object):

    def open_spider(self, spider):
        self.engine = create_engine('sqlite:///data.sqlite')
        items.Model.metadata.create_all(self.engine)
        session_marker = sessionmaker(bind=self.engine)
        self.session = session_marker()

    def close_spider(self, spider):
        self.session.close()

    def process_item(self, item, spider):
        #cls = item.__class__
        #if self.session.query(cls).filter(cls.id==item.id and cls.date==item.id).count():
        #    self.session.update(item)
        #else:
        #    self.session.add(item)
        self.session.merge(item)
        self.session.commit()
        return item
