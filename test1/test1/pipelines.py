# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from scrapy.conf import settings


class Test1Pipeline(object):
    def __init__(self):
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_SHEETNAME"]

        # 创建数据库链接
        client = MongoClient(host=host, port=port)
        # 指定数据库
        my_db = client[dbname]
        # 存放数据的数据库表名
        self.collection = my_db[sheetname]

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
