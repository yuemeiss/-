# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class SpidertestPipeline(object):
    def __init__(self, host, user, pwd, db):
        self.client = pymysql.Connect(host, user, pwd, db, charset='utf8')
        self.cursor = self.client.cursor()

    @classmethod
    def from_crawler(cls, crawler):
        host = crawler.settings['MYSQL_HOST']
        user = crawler.settings['MYSQL_USER']
        pwd = crawler.settings['MYSQL_PWD']
        db = crawler.settings['MYSQL_DB']
        return cls(host, user, pwd, db)

    def process_item(self, item, spider):
        data = dict(item)
        sql, parmaars = item.insert_db_by_data(data)
        # print(parmaars)
        try:
            self.cursor.execute(sql, parmaars)
            self.client.commit()
        except Exception as err:
            self.client.rollback()
            print(err)
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.client.close()