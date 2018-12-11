# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class ZhihuproPipeline(object):

    def __init__(self, host, user, pwd, db, charset):
        # 创建数据库连接
        self.client = pymysql.Connect(host, user, pwd, db, charset=charset)
        # 创建爱你游标执行sql语句
        self.cursor = self.client.cursor()

    def start_spider(self, spider):
        """
        爬虫开启的时候会调用一次
        :param spider:
        :return:
        """
        pass

    @classmethod
    def from_crawler(cls, crawler):
        host = crawler.settings['MYSQL_HOST']
        user = crawler.settings['MYSQL_USER']
        pwd = crawler.settings['MYSQL_PWD']
        db = crawler.settings['MYSQL_DB']
        charset = crawler.settings['MYSQL_CHARSET']

        return cls(host, user, pwd, db, charset)

    def process_item(self, item, spider):

        sql, data = item.insert_db_by_data(dict(item))


        try:
            self.cursor.execute(sql, data)
            self.client.commit()
        except Exception as err:
            print('======================================',err)
            self.client.rollback()

        return item

    def close_spider(self, spider):
        """
        爬虫结束的时候会调用一次
        :param spider:
        :return:
        """
        self.cursor.close()
        self.client.close()
