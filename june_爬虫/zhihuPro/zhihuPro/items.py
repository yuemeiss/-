# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuproItem(scrapy.Item):
    # 问题作者ｉｄ
    author_id_id = scrapy.Field()
    # 问题ｉｄ
    id = scrapy.Field()
    # title
    title = scrapy.Field()
    # 问题创建时间
    pub_time = scrapy.Field()
    # 问题的回答数量
    answer_count = scrapy.Field()
    # 关注的数量
    follower_count = scrapy.Field()
    # 问题的描述
    intro = scrapy.Field()

    def insert_db_by_data(self, subdict):
        sql, data = get_sql_parmase_by_dict(subdict, 'question')

        return sql, data


class ZhihuTagsItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    intro = scrapy.Field()
    tag_url = scrapy.Field()

    def insert_db_by_data(self, subdict):
        sql, data = get_sql_parmase_by_dict(subdict, 'tags')

        return sql, data


class ZhihuAnswerItem(scrapy.Item):
    # 回答ｉｄ
    id = scrapy.Field()
    # 问题ｉｄ
    qid_id = scrapy.Field()
    # 作者ｉｄ
    ahthor_id_id = scrapy.Field()
    # 内容
    content = scrapy.Field()
    # 发布时间
    pub_time = scrapy.Field()
    # 更新时间
    update_time = scrapy.Field()
    # 赞同数量
    endorse = scrapy.Field()
    # 评论数量
    comment_num = scrapy.Field()

    def insert_db_by_data(self, subdict):
        sql, data = get_sql_parmase_by_dict(subdict, 'answer')

        return sql, data


class ZhihuCommentItem(scrapy.Item):
    id = scrapy.Field()
    # 回答ｉｄ
    aid_id = scrapy.Field()
    author_id_id = scrapy.Field()
    author_name = scrapy.Field()
    # 创建时间
    pub_time = scrapy.Field()
    content = scrapy.Field()
    like_num = scrapy.Field()
    # 子评论
    child_comment_count = scrapy.Field()
    child_comments = scrapy.Field()

    def insert_db_by_data(self, subdict):
        sql, data = get_sql_parmase_by_dict(subdict, 'comment')

        return sql, data


class ZhihuAuthorItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    # 性别
    gender = scrapy.Field()
    # 居住地
    address = scrapy.Field()
    add_desc = scrapy.Field()
    headline = scrapy.Field()
    # 简介
    intro = scrapy.Field()
    # 学校
    school = scrapy.Field()
    # 职业
    jobname = scrapy.Field()
    # 回答的问题数量
    answer_count = scrapy.Field()
    # 提出问题的数量
    question_count = scrapy.Field()
    # 被关注的数量
    follower_count = scrapy.Field()

    def insert_db_by_data(self, subdict):
        sql, data = get_sql_parmase_by_dict(subdict, 'author')

        return sql, data

# 多对多关系表
class ZhihuManyItem(scrapy.Item):
    question_id = scrapy.Field()
    tags_id = scrapy.Field()

    def insert_db_by_data(self, subdict):
        sql, data = get_sql_parmase_by_dict(subdict, 'tags_qtype')

        return sql, data


def get_sql_parmase_by_dict(subdict, tablename):
    sql = '''INSERT INTO %s(%s) VALUES (%s)''' % (tablename, ','.join(subdict.keys()), ','.join(['%s'] * len(subdict)))

    data = [value for key, value in subdict.items()]
    return sql, data
