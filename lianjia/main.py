# -*- coding: utf-8 -*-
from scrapy import cmdline
import sys, os

#argv = None
#if len(sys.argv) == 1:
#	#argv = [sys.argv[0], 'crawl', 'community']
#	#argv = [sys.argv[0], 'crawl', 'all_community']
#    argv = [sys.argv[0], 'crawl', 'deal_community']
#cmdline.execute(argv)



from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy import log
from spiders import community_deal_spider
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
import items
import dbhelper as db
from sqlalchemy import Column, Integer, String, Text, Float, create_engine, and_, or_

settings = get_project_settings()
configure_logging(settings)
runner = CrawlerRunner(settings)
crawl_level = 'p3'

@defer.inlineCallbacks
def crawl():
	original_items = db.session.query(items.OriginalCommunityItem).filter(and_(items.OriginalCommunityItem.start_url.like('%/{}/%'.format(crawl_level)), items.OriginalCommunityItem.date == '17-03-22'))\
		.all()
	for ind, item in enumerate(original_items[:1000], start=1):#900 now and 
		print 'scrapying deal items for', item.id, ind
		yield runner.crawl(community_deal_spider.CommunityDealSpider, item.id)
	reactor.stop()
crawl()
reactor.run()
print 'done'