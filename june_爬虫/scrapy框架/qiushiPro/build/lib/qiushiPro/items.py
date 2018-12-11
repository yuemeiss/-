# -*- coding: utf-8 -*-

# Define here the models for your scraped Fields
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/Fields.html

from scrapy import Field


class QiushiproField(Field):
    # 作者
    clsid_id = Field()
    title = Field()
    # 段子内容
    content = Field()
    # 图片
    img_url = Field()
    # 本地图片
    localImgPath = Field()
    # 好笑
    funny_num = Field()
    # 评论
    comment_num = Field()
    comment_list = Field()


    def insert_db_by_data(self, subdict):

        sql, data = get_sql_parmase_by_dict(subdict, 'spiderapp_qiushipro')

        return sql,data


class JuziconproField(Field):
    tags = Field()
    clsid = Field()
    # 作品图片
    img_url = Field()
    # 本地图片
    localImgPath = Field()
    title = Field()
    intro = Field()
    content_list = Field()
    #数据库创建命令
    #create database junePro charset=utf8;
    # create
    # table
    # works(
    # -> id
    # int
    # auto_increment,
    # -> clsid
    # int
    # default
    # 1,
    # -> tags
    # varchar(255),
    # -> img_url
    # varchar(255),
    # -> localImgPath
    # varchar(255),
    # -> title
    # varchar(150),
    # -> intro
    # text,
    # -> content_list
    # text,
    # -> primary
    # key(id),
    # -> foreign
    # key(clsid)
    # references
    # clstable(id));

    def insert_db_by_data(self, subdict):

        sql, data = get_sql_parmase_by_dict(subdict, 'spiderapp_juziconpro')

        return sql,data
class JuzitagsField(Field):
    tags = Field()
    clsid = Field()
    # 作品图片
    img_url = Field()
    # 本地图片
    localImgPath = Field()
    title = Field()
    intro = Field()
    content_list = Field()
    #最新
    con_time = Field()
    #句子去重id
    uuid = Field()
    def insert_db_by_data(self, subdict):

        sql, data = get_sql_parmase_by_dict(subdict, 'spiderapp_juzitagtable')

        return sql,data


def get_sql_parmase_by_dict(subdict, tablename):
    sql = '''INSERT INTO %s(%s) VALUES (%s)''' % (tablename, ','.join(subdict.keys()), ','.join(['%s'] * len(subdict)))

    data = [value for key, value in subdict.items()]
    return sql,data
