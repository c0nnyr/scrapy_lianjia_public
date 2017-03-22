# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import items
import dbhelper as db

class LianjiaPipeline(object):

    def open_spider(self, spider):
        #self.json_file = open('data.json', 'w')
        pass

    def close_spider(self, spider):
        #self.json_file.close()
        pass

    def process_item(self, item, spider):
        #保存数据库
        db.session.merge(item)
        db.session.commit()

        #保存json文件
        #self.json_file.write(item.original_data)
        #self.json_file.write('\n')
        #self.json_file.flush()

        return item
