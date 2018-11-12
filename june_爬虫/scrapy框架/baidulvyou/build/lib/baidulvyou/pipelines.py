# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 将数据存储到mongo
import  pymongo
class BaidulvyouPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient('127.0.0.1',27017)
        #选择数据库
        self.db = self.client['baidulvyou']
        #选择数据库下的集合
        self.col = self.db['lvyouinfo']

    def process_item(self,item,spider):
        #将数据存入集合
        self.col.insert(dict(item))

    def close_spider(self,spider):
        self.client.close()