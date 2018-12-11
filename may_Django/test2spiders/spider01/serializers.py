#-*- coding:utf-8 -*-        
# @time  :18-11-11 下午12:19    
# @Author :董振兵                
# @File   :serializers
from rest_framework import serializers
from .models import Qiushipro

class QiushiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qiushipro
        fields = (
            'id',
            'title',
            'content',
            'img_url',
            'localImgPath',
            'funny_num',
            'comment_num',
            'comment_list',
            'operator',
        )