# -*- coding: utf-8 -*-
import items
import dbhelper as db
from sqlalchemy import and_

def diff_yestoday():
	today_items = db.session.query(items.HouseItem).filter(items.HouseItem.date == items.HouseItem.get_today_str()).all()
	yestoday_items = db.session.query(items.HouseItem).filter(items.HouseItem.date == items.HouseItem.get_today_str(-1)).all()
	print 'today total houses {}'.format(len(today_items))
	for today_item in today_items:
		for yestoday_item in yestoday_items:
			if today_item.id == yestoday_item.id:
				delta_price = today_item.total_price - yestoday_item.total_price
				today_state = db.session.query(items.HouseStateItem).filter(and_(items.HouseStateItem.id == today_item.id, items.HouseStateItem.date == items.HouseStateItem.get_today_str())).first()
				yestoday_state = db.session.query(items.HouseStateItem).filter(and_(items.HouseStateItem.id == today_item.id, items.HouseStateItem.date == items.HouseStateItem.get_today_str(-1))).first()
				delta_see_count = today_state.see_count - yestoday_state.see_count
				print 'for id {}, area {}, price_per_sm {}, total price {} see_count {}, diff price {}, diff see_count {}'.\
					format(today_item.id, today_item.house_size, today_item.price, today_item.total_price, today_state.see_count, delta_price, delta_see_count)
				if delta_price != 0:
					print 'http://cd.lianjia.com/ershoufang/{}.html'.format(today_item.id)
				break
		else:
			print 'id {} is new today'.format(today_item.id)

