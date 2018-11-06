# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaidulvyouItem(scrapy.Item):
    # 标题
    address = scrapy.Field()
    # 图片
    img_url=scrapy.Field()
    #评分
    grade=scrapy.Field()
    #评论数量
    comment_num = scrapy.Field()
    #简介
    intro = scrapy.Field()
    #建议
    best_offer = scrapy.Field()
    #评论列表
    comment_list = scrapy.Field()
    # bcom_content  = scrapy.Field()
    # com_userName=scrapy.Field()
    # com_pub_time = scrapy.Field()
    # available = scrapy.Field()
    # replynums=scrapy.Field()

