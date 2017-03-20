# -*- coding: utf-8 -*-
from scrapy import cmdline
import sys, os
argv = None
if len(sys.argv) == 1:
	argv = [sys.argv[0], 'crawl', 'all_community']
cmdline.execute(argv)