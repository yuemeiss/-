# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import scrapy
import pymongo
import pymysql

from scrapy.contrib.pipeline.images import ImagesPipeline
# from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings

image_store = get_project_settings().get('IMAGES_STORE')


class QiushiImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if 'img_url' not in item.keys():
            return None
        # 截取图片地址,发起请求
        if item['img_url'] != '0':
            if 'http:' in item['img_url']:
                imageurl = item['img_url']
            else:
                imageurl = 'https:' + item['img_url']
            yield scrapy.Request(url=imageurl,dont_filter=False)

    def item_completed(self, results, item, info):
        paths = [subdict['path'] for ok, subdict in results if ok]
        if paths:
            # print('xxxxxxxxxxxxxxxxxxxxxxxxxx',paths[0][5:-5:2])
            os.rename(image_store + '/'+ paths[0], image_store + '/'+ str(item['clsid_id']) + '/' + paths[0][5:-5:2] + '.jpg')
            item['localImgPath'] = image_store + '/' + str(item['clsid_id']) + '/'+ paths[0][5:-5:2] + '.jpg'
            # except Exception as err:
            #     item['localImgPath'] = '未知'
            #     return item
        else:
            item['localImgPath'] = '未知'
        return item

class JuziconproPipeline(object):
    def __init__(self,host,user,pwd,db):
        self.client = pymysql.Connect(host,user,pwd,db,charset='utf8')
        self.cursor = self.client.cursor()
    @classmethod
    def from_crawler(cls,crawler):
        host = crawler.settings['MYSQL_HOST']
        user = crawler.settings['MYSQL_USER']
        pwd = crawler.settings['MYSQL_PWD']
        db = crawler.settings['MYSQL_DB']
        return cls(host,user,pwd,db)
    def process_item(self,item,spider):
        data = dict(item)
        sql,parmaars = item.insert_db_by_data(data)
        try:
            self.cursor.execute(sql,parmaars)
            self.client.commit()
        except Exception as err:
            self.client.rollback()
            print(err)
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.client.close()



class QiushiproPipeline(object):

        def __init__(self, host, port, dbname):
            # 创建mongo的客户端连接
            self.client = pymongo.MongoClient(host, port)
            # 获取数据库（切换到指定数据库）
            self.db = self.client[dbname]

        @classmethod
        def from_crawler(cls, crawler):
            host = crawler.settings['MONGO_HOST']
            port = crawler.settings['MONGO_PORT']
            dbname = crawler.settings['MONGO_DB']

            return cls(host, port, dbname)

        def process_item(self, item, spider):
            # 获取集合名称
            col_name = item.get_collection_name_by_data()
            # 获取数据库下的集合
            col = self.db[col_name]
            # 王几何中插入数据
            col.insert(dict(item))

            return item

        def close_spider(self, spider):
            # 关闭数据库连接
            self.client.close()
