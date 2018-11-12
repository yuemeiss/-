# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

#指定scrapy-redis 的过滤器组件,不在使用scrapy框架默认的过滤器组件了.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

#指定scrapy-redis 不在使用scrapy框架默认的调度器组件了
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

#允许恢复和暂停
SCHEDULER_PERSIST = True

#scrapy的三种requset队列模式
#1.一般通常都是会用这种,是默认的队列模式,有自己的优先级顺序
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#2.启用了队列的形式,先进先出,(相当于堆的结构)
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#3.相当于栈的结构,先进后出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

#设置ua
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

#默认激活了'scrapy_redis.pipelines.RedisPipeline'
#将item
ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.

# DOWNLOAD_DELAY = 1

#指定redis的相关配置
#指定要存储的redis  主机IP
REDIS_HOST = '127.0.0.1'

#指定redis的端口号
REDIS_PORT = 6379
#1.激活自定义管道
#2.驱虫

