# -*- coding: utf-8 -*-

import items
import dbhelper as db
import re

for item in db.session.query(items.OriginalCommunityItem).all():
    item.start_url = re.sub('pg\d*', '', item.start_url)
    db.session.merge(item)
    db.session.commit()
