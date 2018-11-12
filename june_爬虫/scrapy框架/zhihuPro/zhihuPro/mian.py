#-*- coding:utf-8 -*-        
# @time  :18-11-7 下午6:31    
# @Author :董振兵                
# @File   :mian
import sys,os
from scrapy.cmdline import execute
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy','crawl','zhihu'])