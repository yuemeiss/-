# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qiushiPro.items import QiushiproField

class QiushibaikeSpider(CrawlSpider):
    name = 'qiushibaike'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/',
                  'https://www.qiushibaike.com/hot/',
                  'https://www.qiushibaike.com/text/',
                  'https://www.qiushibaike.com/history/',
                  'https://www.qiushibaike.com/pic/',
                  'https://www.qiushibaike.com/textnew/',
                  'https://www.qiushibaike.com/imgrank/'
                  ]
    # https://ishuo.cn/duanyu
    # http://www.shuoshuokong.com/ 说说控
    # https://www.juzicon.com/mip/authors/fd144490-0be2-453e-b708-3811539a3d20 句子控
    # 心理学吧

    rules = [
        # # 分类url
        # Rule(
        #     LinkExtractor(
        #         allow=r'm/.+/$',
        #         restrict_css=('div#menu a',)
        #     ),
        #     # callback='parse_item',
        #     follow=False
        # ),
        # 下一页
        Rule(
            LinkExtractor(
                allow=r'/.*\d+/$',
                restrict_xpaths='//ul[@class="pagination"]/li/a'
            ),
            follow=True
        ),
        # 提取详情页
        Rule(
            LinkExtractor(
                allow=r'/a.*',
                restrict_xpaths='//div[@id="content-left"]//a[@class="contentHerf"]'
            ),
            callback='parse_detaile',
            follow=False
        ),

    ]
    def parse_detaile(self, response):
        print(response.url)
        joke = QiushiproField()
        # 作者
        joke['title'] = response.xpath('//div[contains(@class,"author")]//h2/text()').extract_first('未知')
        # print(title)
        joke['clsid'] = 5
        # 段子内容
        joke['content'] = ','.join(response.xpath('//div[@class="content"]/text()').extract()).replace(' ','').replace('\n','')
        #图片
        joke['img_url'] = response.xpath('//div[@class="thumb"]/img/@src').extract_first('空')
        # print(img_url)
        # print(content)
        # 好笑
        joke['funny_num'] = response.xpath('//div[@class="stats"]//i/text()').extract_first('0')
        # print(funny_num)

        com_list = []

        com_obj = response.xpath('//div[@class="comments-list"]/div/div')
        print(len(com_obj))
        for com in com_obj:
            com_dic = {}
            com_dic['userName'] = com.css('div.main-name div.cmt-name::text').extract_first('未知').replace('\n','')
            com_dic['userAge'] = com.css('div.main-name div.articleGender::text').extract_first('未知')
            com_dic['likeNum'] = ''.join(com.css('div.likenum ::text').extract()).replace(' ','').replace('\n','')
            com_dic['text'] = com.css('div.main-text::text').extract_first('未知').strip()
            com_list.append(com_dic)
        # 评论
        joke['comment_list'] = str(com_list)
        # print(comment_list)
        yield joke








