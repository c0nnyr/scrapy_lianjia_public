# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import items

class LianjiaPipeline(object):

    def open_spider(self, spider):
        #self.engine = create_engine('sqlite:///data.sqlite')
        #items.Model.metadata.create_all(self.engine)
        #session_marker = sessionmaker(bind=self.engine)
        #self.session = session_marker()

        self.json_file = open('data.json', 'w')

    def close_spider(self, spider):
        items.g_session.close()
        self.json_file.close()

    def process_item(self, item, spider):
        #保存数据库
        items.g_session.merge(item)
        items.g_session.commit()

        #保存json文件
        self.json_file.write(item.original_data)
        self.json_file.write('\n')
        self.json_file.flush()

        return item
