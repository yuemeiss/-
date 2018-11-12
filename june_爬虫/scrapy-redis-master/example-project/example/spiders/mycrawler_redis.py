from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider
from example.items import BaidulvyouItem


class MyCrawler(RedisCrawlSpider):
    """
    爬虫文件中只有两个地方跟我们单机版爬虫不一样
    1.继承的类不一样
    2.少了一个start_urls参数,多了一个redis_key:可根据这个key从redis数据库中获取爬虫的起始任务
    Spider that reads urls from redis queue (myspider:start_urls).
    """
    name = 'mycrawler_redis'
    redis_key = 'my_start_urls'
    allowed_domains = ['lvyou.baidu.com']
    rules = (
        # 下一页
        Rule(LinkExtractor(allow=r'\?rn=\d+&pn=\d+', restrict_xpaths=('//span[@class="pagelist"]//a[@class="nslog"]',)),
             follow=True),
        # 详情页
        Rule(LinkExtractor(allow=r'/\w+/', restrict_xpaths=('//li[@class="filter-result-item "]//h3/a',)),
             callback='parse_data', ),

    )

    # 动态获取要爬取的域 ,一般不使用它 我们会使用allowed_domains
    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(MyCrawler, self).__init__(*args, **kwargs)
    def parse_data(self, response):
        # print(response.status)
        # response
        baidu = BaidulvyouItem()
        baidu['address'] = response.xpath('//div[@class="dest-name "]//a/text()').extract_first()
        baidu['img_url'] = response.xpath('//ul[@id="J_pic-slider"]//a/img/@src').extract()
        baidu['grade'] = ''.join(response.xpath('//div[@class="main-score"]/text()').extract()).replace('\n',
                                                                                                        '').replace(' ',
                                                                                                                    '')
        baidu['comment_num'] = response.xpath(
            '//div[@class="main-score"]/a[@class="remark-count"]/text()').extract_first()
        baidu['intro'] = response.xpath(
            '//div[@class="main-info-wrap"]//div[@class="main-desc"]/p/text()').extract_first().strip()
        baidu['best_offer'] = '-'.join(response.xpath('//div[@class="main-intro"]//text()').extract()).replace('\n',
                                                                                                               '').replace(
            ' ', '')
        baidu['comment_list'] = []
        comment_list = response.xpath('//div[@class="remark-list"]/div')
        for com in comment_list:
            comdict = {}
            comdict['com_content'] = com.xpath('.//div[@class="ri-body"]//text()').extract()
            comdict['com_userName'] = com.xpath('.//div[@class="ri-avatar-wrap"]/a/@title').extract()
            comdict['com_pub_time'] = com.xpath(
                './/div[@class="ri-header"]/div[@class="ri-time"]/text()').extract_first()
            comdict['available'] = com.xpath('.//a[@class="ri-dig ri-dig-available"]/span/text()').extract()
            comdict['replynums'] = com.xpath('.//a[@class="ri-comment"]/span/text()').extract()
            baidu['comment_list'].append(comdict)
        yield baidu
