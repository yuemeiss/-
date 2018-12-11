# -*- coding: utf-8 -*-
import requests
import json, re
# from urllib.parse import quote
from zhihuPro.items import *
from scrapy_splash import SplashRequest

# from scrapy_splash import SplashResponse

script = """
function main(splash, args)
  splash:go("https://www.zhihu.com")
  btn = splash:select(".SignContainer-switch span")
  btn:mouse_click()
  splash:wait(3)
  input = splash:select(".SignFlow-accountInput input")
  input:send_text("18235056870")
  splash:wait(1)
  pwd = splash:select(".SignFlow-password input")
  pwd:send_text("lwy123456")
  splash:wait(1)
  loginBtn = splash:select(".SignFlow-submitButton")
  loginBtn:mouse_click()
  splash:wait(3)
  return splash:get_cookies()
end
"""


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    base_url = 'https://www.zhihu.com/'
    cookie = None
    myheaders = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }

    # dzb632816
    def start_requests(self):
        try:
            with open('cookie.json', 'r') as f:
                self.cookie = json.loads(f.read())
            yield scrapy.Request(
                url=self.base_url,
                callback=self.parse_page, cookies=self.cookie)
        except:
            yield SplashRequest(url=self.base_url, callback=self.parse_login, endpoint='execute', args={
                'lua_source': script,
            })

    def parse_login(self, response):
        py_list = json.loads(response.text)
        # print(type(py_list))
        cookie = {i['name']: i['value'] for i in py_list}
        with open('cookie.json', 'w') as file:
            json.dump(cookie, file, ensure_ascii=False, indent=4)
        yield scrapy.Request(url=self.base_url, callback=self.parse_page, cookies=cookie)

    def parse_page(self, response):
        # 18235056870   lwy123456
        # api_url = 'https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=94b179cd0fb867a3729b0af574a1a77d&desktop=true&limit=7&action=down&after_id=0'
        # https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=94b179cd0fb867a3729b0af574a1a77d&desktop=true&limit=7&action=down&after_id=13
        session_token = response.xpath('.').re_first('.*?session_token=(.*?)&')
        api_url = 'https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token={}&desktop=true&limit=7&action=down&after_id=0'.format(session_token)
        yield scrapy.Request(url=api_url, callback=self.parse_json, cookies=self.cookie)

    def parse_json(self, response):
        datas = json.loads(response.text)
        for i in datas['data']:
            question_item = ZhihuproItem()
            # with open('bug.json', 'w') as file:
            #     json.dump(i['target'], file, ensure_ascii=False, indent=4)
            if 'question' in i['target'].keys():
                # 问题作者ｉｄ
                question_item['author_id_id'] = i['target']['author']['id']
                if question_item['author_id_id'] != '0':
                    author_url = 'https://api.zhihu.com/people/' + question_item['author_id_id']
                    #因外键关系　使用requests
                    resp = requests.get(author_url,headers=self.myheaders,cookies=self.cookie)
                    # print(resp.text)
                    yield self.parse_author(resp.text)
                # 问题ｉｄ
                question_item['id'] = i['target']['question']['id']
                # title
                question_item['title'] = i['target']['question']['title']
                # 问题创建时间
                question_item['pub_time'] = i['target']['question']['created']
                # 问题的回答数量
                question_item['answer_count'] = i['target']['question']['answer_count']
                # 关注的数量
                question_item['follower_count'] = i['target']['question']['follower_count']
                # 问题的描述
                question_item['intro'] = i['target']['question']['excerpt']

                yield question_item

                # 问题标签
                # https: // www.zhihu.com / question / 296894584
                tags_url = 'https://www.zhihu.com/question/' + str(question_item['id'])
                yield scrapy.Request(url=tags_url, callback=self.parse_tag, meta={'que_id': question_item['id']})
                # 回答
                answer_url = 'https://www.zhihu.com/api/v4/questions/' + str(question_item[
                                                                                 'id']) + '/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=20&offset=0&sort_by=default'
                yield scrapy.Request(url=answer_url, callback=self.parse_answer)
                # 获取问题作者信息

                # break
                # print(que_author_id,id,title,pub_time,answer_count,follower_count,intor,tags)
        # 下一页
        # yield scrapy.Request(url=datas['paging']['next'],callback=self.parse_json)

    def parse_answer(self, response):
        answer = json.loads(response.text)
        for a in answer['data']:
            answer_item = ZhihuAnswerItem()
            # 回答ｉｄ
            answer_item['id'] = a['id']
            # 问题ｉｄ
            answer_item['qid_id'] = a['question']['id']
            # 作者ｉｄ
            answer_item['ahthor_id_id'] = a['author']['id']
            if answer_item['ahthor_id_id'] != "0":
                # 作者ｕｒｌ  获取作者信息
                author_url = 'https://api.zhihu.com/people/' + answer_item['ahthor_id_id']
                print(author_url)
                resp = requests.get(author_url,headers=self.myheaders, cookies=self.cookie)
                yield self.parse_author(resp.text)
            # 内容
            answer_item['content'] = a['content']
            # print('--------------------------',answer_item['content'])
            # 发布时间
            answer_item['pub_time'] = a['created_time']
            # 更新时间
            answer_item['update_time'] = a['updated_time']
            # 赞同数量
            answer_item['endorse'] = a['voteup_count']
            # 评论数量
            answer_item['comment_num'] = a['comment_count']

            yield answer_item
            # 评论
            comment_url = 'https://www.zhihu.com/api/v4/answers/{}/root_comments?include=data%5B*%5D.author%2Ccollapsed%2Creply_to_author%2Cdisliked%2Ccontent%2Cvoting%2Cvote_count%2Cis_parent_author%2Cis_author&order=normal&limit=30&offset=0&status=open'.format(
                answer_item['id'])
            print(comment_url)
            yield scrapy.Request(url=comment_url, callback=self.parse_comment,meta={'ans_id':answer_item['id']})


            # break
        #下一页
        # yield scrapy.Request(url=answer['paging']['next'],callback=self.parse_json)
    def parse_comment(self, response):
        comment_list = json.loads(response.text)['data']
        # print(comment_list)
        uid = response.meta['ans_id']
        for comment in comment_list:
            comment_item = ZhihuCommentItem()
            comment_item['id'] = comment['id']
            #回答ｉｄ
            comment_item['aid_id'] = uid
            comment_item['author_id_id'] = comment['author']['member']['id']
            if comment_item['author_id_id'] != "0":
                # 作者ｕｒｌ  获取作者信息
                author_url = 'https://api.zhihu.com/people/' + comment_item['author_id_id']
                resp = requests.get(author_url,headers=self.myheaders, cookies=self.cookie)
                yield self.parse_author(resp.text)
            # print(info)
            comment_item['author_name'] = comment['author']['member']['name']
            #创建时间
            comment_item['pub_time'] = comment['created_time']
            comment_item['content'] = comment['content']
            comment_item['like_num'] = comment['vote_count']
            #子评论
            comment_item['child_comment_count'] = comment['child_comment_count']
            #只取　子评论的　作者名和内容
            comment_item['child_comments'] = str({s['author']['member']['name']:s['content'] for s in comment['child_comments']})
            # print(comment_item)
            yield comment_item


    def parse_author(self, res):
        author = json.loads(res)
        print(author)
        if 'error' in author.keys():
            print('该用户不存在')
            return False
        author_item = ZhihuAuthorItem()
        author_item['id'] = author['id']
        author_item['name'] = author['name']
        #性别
        author_item['gender'] = author['gender']
        # 居住地
        if 'location' in author.keys():
            author_item['address'] = author['location'][0]['name']
            author_item['add_desc'] = author['location'][0]['introduction']
        else:
            # 居住地
            author_item['address'] = '无'
            author_item['add_desc'] = '无'

        author_item['headline'] = author['headline']
        #简介
        author_item['intro'] = author['description']
        #学历
        if 'education' in author.keys():
            author_item['school'] = author['education'][0]['name']

        else:
            author_item['school'] = '无'

        #职业
        author_item['jobname'] = author['business']['name']
        #回答的问题数量
        author_item['answer_count'] = author['answer_count']
        #提出问题的数量
        author_item['question_count'] = author['question_count']
        #被关注的数量
        author_item['follower_count'] = author['follower_count']
        # print(author_item)
        return author_item

    def parse_tag(self, response):
        re_obj = re.compile('"topics":(\[.*?\]),', re.S)
        tags = re.findall(re_obj, response.text)
        tag_list = json.loads(tags[0])
        # print('===============================', tag_list)
        # 多对多
        qid = response.meta['que_id']
        # 获取标签
        for tag in tag_list:
            tag_item = ZhihuTagsItem()
            many_item = ZhihuManyItem()
            tag_item['id'] = tag['id']
            tag_item['name'] = tag['name']
            tag_item['intro'] = tag['excerpt']
            tag_item['tag_url'] = tag['url']
            many_item['question_id'] = qid
            many_item['tags_id'] = tag['id']
            yield tag_item
            yield many_item
            # print(tag_item)
            # yield tag_item
