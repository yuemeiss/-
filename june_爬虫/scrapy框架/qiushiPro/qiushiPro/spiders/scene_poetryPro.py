# -*- coding: utf-8 -*-
import scrapy, re, json
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qiushiPro.items import JuziconproField, JuzitagsField


class ScenePoetryproSpider(CrawlSpider):
    name = 'scene_poetryPro'
    allowed_domains = ['juzicon.com']
    start_urls = ['https://www.juzicon.com/channels']
    page = 0

    rules = (
        # 分类
        Rule(LinkExtractor(
            allow=r'.*?/.*',
            restrict_xpaths=(
                '//dl[@class="_1WBovXLyVvmGfTYtiw8Uf_0"][2]//a', '//dl[@class="_1WBovXLyVvmGfTYtiw8Uf_0"][4]//a'),
        ), callback='parse_page', follow=False),
        # 标签分类
        Rule(LinkExtractor(
            allow=r'.*?/.*',
            restrict_xpaths=(
                '//dl[@class="_1WBovXLyVvmGfTYtiw8Uf_0"][3]//a',),
        ), callback='parse_tags', follow=False),

    )

    def parse_page(self, response):
        print('=========', response.url)
        work = JuziconproField()
        work['tags'] = response.xpath('//div/span/h1/text()').extract_first('其他')
        if 'channels' in response.url:
            work['clsid_id'] = 3
        else:
            work['clsid_id'] = 2
        loads = []
        con_list = response.xpath('//section[@class="_3kJ_X8s2Fl1RMezfKtlens_0"]')
        for con in con_list:
            con_dict = {}
            con_dict['content'] = ','.join(
                con.xpath('.//div[@class="_1M-w2BKM75D4AvckCH596S_0"]//span/text()').extract()).replace(' ',
                                                                                                        '').replace(
                '\n', '')
            con_dict['like'] = con.xpath('.//span[@class="_2NoMli8aRzS3nQig3U2aBr_0"]/text()').extract_first()
            con_dict['comment'] = con.xpath('.//span[@class="_3buMK5elpnD6oocG5zL0Z_0"]/text()').extract_first()
            loads.append(con_dict)
        work['content_list'] = str(loads)
        # print(loads)
        yield work

        page_url = response.xpath('//button[@class="btn-next"]/a/@href').extract_first()
        print(page_url)
        if page_url:
            yield response.follow(url=page_url, callback=self.parse_page)

    # def parse_tags(self, response):
    #     bb = response.url
    #     self.page += 1
    #     if 'posts' in bb:
    #         data_list = json.loads(response.text)['data']['list']
    #         for dat in data_list:
    #             tagcls = JuzitagsField()
    #             if bool(dat['tags']):
    #                 tagcls['tags'] = ','.join(dat['tags'])
    #             else:
    #                 tagcls['tags'] = '其他'
    #             # print(tagcls['tags'])
    #             tagcls['clsid_id'] = 4
    #             tagcls['con_time'] = dat['createdAt']
    #             tagcls['content_list'] = str([dat['content'], dat['referWorksName'], dat['cntComment'], dat['cntLike']])
    #             # print(tagcls['content_list'])
    #             # 句子去重id
    #             tagcls['uuid'] = dat['uuid']
    #             if 'creator' in dat.keys():
    #                 tagcls['img_url'] = dat['creator']['avatar']
    #                 print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', tagcls['img_url'])
    #                 tagcls['title'] = dat['creator']['nickname']
    #                 tagcls['intro'] = dat['creator']['intro']
    #             yield tagcls
    #         if self.page < 100:
    #             yield scrapy.Request(url=bb + '?start=' + str(self.page), callback=self.parse_tags)
    #     else:
    #         ss = re.findall('discovery(.*)', bb)[0]
    #         api_url = 'https://api.juzicon.com/n0/discovery/posts' + ss
    #         self.page = 0
    #         yield scrapy.Request(url=api_url, callback=self.parse_tags)
