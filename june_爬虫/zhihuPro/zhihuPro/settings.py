# -*- coding: utf-8 -*-

# Scrapy settings for zhihuPro project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuPro'

SPIDER_MODULES = ['zhihuPro.spiders']
NEWSPIDER_MODULE = 'zhihuPro.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihuPro (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihuPro.middlewares.ZhihuproSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihuPro.middlewares.ZhihuproDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zhihuPro.pipelines.ZhihuproPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


#scrapy-splash 相关配置
SPLASH_URL = 'http://localhost:8050'

DOWNLOADER_MIDDLEWARES = {
    'zhihuPro.middlewares.ZhihuProxyMiddleware':543,
    'zhihuPro.middlewares.RandomCookiesDownloadMiddlerWare':545,
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'


#数据库信息配置
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PWD = '123456'
MYSQL_DB = 'zhihuApi'
MYSQL_CHARSET = 'utf8mb4'

COOKIES = [
    {
        "_xsrf": "IiQl9ldK0HcwNa9kmWUKvPmUmBV8Toda",
        "_zap": "0fda08d4-63b7-4c7d-93ca-6f9cb997bb6b",
        "q_c1": "02f92fd5ccd549dcbd38f56a9a86ee8c|1543567737000|1543567737000",
        "d_c0": "\"AHDiVUQHmQ6PThqXE99N65Svd_kHdG_oRNo=|1543567729\"",
        "tst": "r",
        "z_c0": "\"2|1:0|10:1543567735|4:z_c0|92:Mi4xS2o3VkN3QUFBQUFBSUdJelJBZVpEaVlBQUFCZ0FsVk5kMGZ1WEFBZFRvZ2pxUFFlN0N1WURzQm9xZXY0UmswTlFR|113a4addf010159d8ea467bd3a082808634cab1cfd4bef893329255fd0d489b5\"",
        "capsion_ticket": "\"2|1:0|10:1543567730|14:capsion_ticket|44:ZTUxN2RjNTBjYzkyNDEwOGE3NDE0Yjg4YTJjYjg2Yzg=|9bbf323ee3e9e77afc6f699ef726065f62610691cb0a6a139de4fb2a8df86d12\"",
        "tgw_l7_route": "170010e948f1b2a2d4c7f3737c85e98c"
    },
    {
        "capsion_ticket": "\"2|1:0|10:1543750705|14:capsion_ticket|44:MDIzOTY5ZDYwMzdiNDYwNzk5N2Q0YmU1ODY0NDAyNTc=|a64b66d9ed0cb37945beeb9202bceba5cadc04f70a09c5d8d61807d0af8c6518\"",
        "tgw_l7_route": "5bcc9ffea0388b69e77c21c0b42555fe",
        "tst": "r",
        "z_c0": "\"2|1:0|10:1543750710|4:z_c0|92:Mi4xWUJRcENRQUFBQUFBY09FUVFzR2JEaVlBQUFCZ0FsVk5OaEx4WEFEQzdvdnBmSTZVdFdrZ1lBT0pXOVR1VE0zVl9n|368398d9da588a15853e7c63f11d61bb7e36838a10555c28aeed7b46d08a56e9\"",
        "_zap": "0e35e307-fc0c-4a6b-8f6b-a7319d2a1376",
        "_xsrf": "mwCQhPLPuHAa6mrlrDGYpvVls1I7ySoE",
        "d_c0": "\"AOBhYULBmw6PTlvJ4Kqf1wBsnz1tqWBiCZM=|1543750704\""
    }
]
