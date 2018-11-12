# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy




class SpidertestItem(scrapy.Item):
    #标题
    dzb_title =scrapy.Field()
    #图片地址
    dzb_imgurl = scrapy.Field()
    #域名
    dzb_domains = scrapy.Field()
    #周排名
    dzb_rank = scrapy.Field()
    #反链数
    dzb_number = scrapy.Field()
    #得分
    dzb_score = scrapy.Field()
    #得分排名
    dzb_srank = scrapy.Field()
    dzb_intro = scrapy.Field()

    def insert_db_by_data(self, subdict):
        sql, data = get_sql_parmase_by_dict(subdict, 'dzb_testdata')

        return sql, data


class Dzb_ClassName(scrapy.Item):
    #类id
    # dzb_id = scrapy.Field()
    #分类名
    dzb_cname = scrapy.Field()
    #分类URL
    dzb_curl = scrapy.Field()
    def insert_db_by_data(self, subdict):
        sql, data = get_sql_parmase_by_dict(subdict, 'dzb_clsname')

        return sql, data

def get_sql_parmase_by_dict(subdict, tablename):
    sql = '''INSERT INTO %s(%s) VALUES (%s)''' % (tablename, ','.join(subdict.keys()), ','.join(['%s'] * len(subdict)))

    data = [value for key, value in subdict.items()]
    return sql,data

