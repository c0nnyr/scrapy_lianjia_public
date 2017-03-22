# -*- coding: utf-8 -*-
from scrapy import cmdline
import sys, os
argv = None
if len(sys.argv) == 1:
	#argv = [sys.argv[0], 'crawl', 'community']
	#argv = [sys.argv[0], 'crawl', 'all_community']
    argv = [sys.argv[0], 'crawl', 'deal_community']
cmdline.execute(argv)