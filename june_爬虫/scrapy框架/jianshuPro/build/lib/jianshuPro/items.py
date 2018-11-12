# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuproItem(scrapy.Item):
    #类名
    classname = scrapy.Field()
    #管理员信息
    admin_list = scrapy.Field()
    #文章标题
    title = scrapy.Field()
    #文章发布时间
    pub_time = scrapy.Field()
    #文章字数
    con_num = scrapy.Field()
    #文章阅读量
    read_num = scrapy.Field()
    #文章评论量
    comment_num = scrapy.Field()
    #文章喜欢数量
    like_num = scrapy.Field()
    #文章赞赏量
    admire_num = scrapy.Field()
    #文章内容
    context = scrapy.Field()
    #作者信息
    author = scrapy.Field()
    def get_collection_name(self,dataDict):
        col_name = ''
        name = dataDict['classname']
        if name == '自然科普':
            col_name = 'kepu'
        elif name == '简书电影':
            col_name = 'jianshu_movie'
        elif name == '摄影':
            col_name = 'photography'
        elif name == '手绘':
            col_name = 'shouhui'
        elif name == '读书':
            col_name = 'read_book'
        elif name == '旅行·在路上':
            col_name = 'travel'
        elif name == '@IT·互联网':
            col_name = 'internet'
        else:
            col_name = 'other'
        return col_name

