#-*- coding:utf-8 -*-        
# @time  :18-11-9 上午12:08    
# @Author :董振兵                
# @File   :main
import sys,os
from scrapy.cmdline import execute
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy','crawl','juzicon_redis'])