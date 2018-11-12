# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
class JianshuproPipeline(object):
    def __init__(self,host,port,dbname):
        #创建数据库链接
        self.client = pymongo.MongoClient(host,port)
        #获取数据库集合
        self.db = self.client[dbname]
    @classmethod
    def from_crawler(cls,crawler):
        host = crawler.settings['MONGO_HOST']
        port = crawler.settings['MONGO_PORT']
        dbname = crawler.settings['MONGO_DB']
        return cls(host,port,dbname)
    def process_item(self, item, spider):
        col_name = item.get_collection_name(dict(item))
        col = self.db[col_name]
        print('==========================集合名:',col_name)
        col.insert(dict(item))
        return item
    def close_spider(self,spider):
        #关闭数据库链接
        self.client.close()