# -*- coding: utf-8 -*-

import items
import dbhelper as db
import re

for item in db.session.query(items.DealItem).all():
    if 'None' in item.start_url:
        db.session.delete(item)
        db.session.commit()
        print 'delete', item.start_url
