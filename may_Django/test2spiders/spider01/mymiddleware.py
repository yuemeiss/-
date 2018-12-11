#-*- coding:utf-8 -*-        
# @time  :18-11-11 下午2:00    
# @Author :董振兵                
# @File   :mymiddleware
from django.utils.deprecation import MiddlewareMixin

class MyMiddleware(MiddlewareMixin):
    """自定义中间件类"""
    def process_request(self, request):
        """产生request对象之后,url匹配之前调用"""
        setattr(request, "_dont_enforce_csrf_checks", True)