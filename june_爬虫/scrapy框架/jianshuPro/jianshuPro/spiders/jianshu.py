# -*- coding: utf-8 -*-
import scrapy, json
import requests

from jianshuPro.items import JianshuproItem


class JianshuSpider(scrapy.Spider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']
    classname = []

    def parse(self, response):

        classifyUrl_li = response.css('div.recommend-collection div::text').extract()
        print(classifyUrl_li)
        #获取分类url列表
        classifyUrl_list = response.xpath('//div[@class="recommend-collection"]/a[@class="collection"]/@href').extract()
        page = 1
        for classifyUrl in classifyUrl_list:
            yield response.follow(url=classifyUrl, callback=self.classify_data, meta={'page': page})
            # break

    def classify_data(self, response):
        pagem = response.meta['page']
        # 分类名: 如 故事,...
        clsname = response.css('div.main-top div.title a.name::text').extract_first()
        # 只请求一次 减少请求次数
        if pagem == 1:
            info_dict = {}
            info_dict['name'] = clsname
            # 管理员信息
            info_id = response.css('div.follow-button::attr(props-data-collection-id)').extract_first()
            administratorUrl = 'https://www.jianshu.com/collections/' + info_id + '/side_list'
            req_headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
            }
            response_info = requests.get(administratorUrl, headers=req_headers)
            user_list = json.loads(response_info.text)['editors']
            # 信息列表
            info_dict['admin_list'] = []
            for user in user_list:
                info_dict['admin_list'].append(user['nickname'])
            self.classname.append(info_dict)
        # 减少请求次数
        admin_info = ''
        for ss in self.classname:
            if ss['name'] == clsname:
                admin_info = ss['admin_list']
        # 详情链接
        detaileUrl_list = response.css('div.content a.title::attr(href)').extract()
        for detaileurl in detaileUrl_list:
            yield response.follow(url=detaileurl, callback=self.detaile_data,
                                  meta={'classify': clsname, 'admin_info': admin_info})
        # 下一页链接
        pageUrl = response.css('ul.note-list::attr(infinite-scroll-url)').extract_first()
        # print(type(pageUrl))
        pagem += 1
        # # 每个分类爬取20页
        if pagem <= 20:
            # print('页码=========',pagem)
            # print('下一页=====',pageUrl)
            yield response.follow(url=pageUrl + '&page=' + str(pagem), callback=self.classify_data,
                                  meta={'page': pagem})

    def detaile_data(self, response):
        js_data = JianshuproItem()
        # 类名
        js_data['classname'] = response.meta['classify']
        # 管理员信息
        js_data['admin_list'] = response.meta['admin_info']
        # 文章标题
        js_data['title'] = response.css('div.article h1::text').extract_first('未知')
        # print(js_data['title'])
        # 文章发布时间
        js_data['pub_time'] = response.css('div.meta span.publish-time::text').extract_first('未知')
        # print(pub_time)
        json_str = response.xpath('//script[@type="application/json"]/text()').extract_first()
        # print('===========================',json_str)
        con_info = json.loads(json_str)['note']
        # 文章字数
        js_data['con_num'] = con_info['public_wordage']
        # print('=================',con_num)
        # 文章阅读量
        js_data['read_num'] = con_info['views_count']
        # 文章评论量
        js_data['comment_num'] = con_info['comments_count']
        # 文章喜欢数量
        js_data['like_num'] = con_info['likes_count']
        # 文章赞赏量
        js_data['admire_num'] = con_info['featured_comments_count']
        # print('字数',con_num,'阅读量',read_num,'评论量',comment_num,'喜欢',like_num,'赞赏',admire_num)
        # 文章内容
        js_data['context'] = response.css('div.show-content-free p::text').extract()
        # 文章图片链接
        # context_img = response.css('div.show-content-free div.image-package div.image-view img::attr(data-original-src)').extract()
        # print(context_img)
        # 作者信息
        js_data['author'] = []
        userInfo = {}
        userInfo['name'] = response.css('div.follow-detail a.title::text').extract_first('未知')
        userInfo['signature'] = response.css('div.signature::text').extract_first('未知')
        userInfo['total_wordage'] = con_info['author']['total_wordage']
        userInfo['followers_count'] = con_info['author']['followers_count']
        userInfo['total_likes_count'] = con_info['author']['total_likes_count']
        js_data['author'].append(userInfo)
        # print(js_data['author'])
        yield js_data
