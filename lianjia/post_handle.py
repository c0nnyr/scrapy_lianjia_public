# -*- coding: utf-8 -*-

import items
import dbhelper as db

for item in db.session.query(items.OriginalCommunityItem).all():
    print item
    break
