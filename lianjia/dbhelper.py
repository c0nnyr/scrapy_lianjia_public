# -*- coding: utf-8 -*-

import scrapy
import datetime, os
from sqlalchemy import Column, Integer, String, Text, Float, create_engine, and_, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Model = declarative_base(name='Model')
engine = create_engine('sqlite:///data.sqlite')
Model.metadata.create_all(engine)
session_marker = sessionmaker(bind=engine)
session = session_marker()
