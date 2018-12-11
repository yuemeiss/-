#-*- coding:utf-8 -*-        
# @time  :18-11-11 上午1:08    
# @Author :董振兵                
# @File   :serializers.py
from rest_framework import serializers
from .models import *

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
        )
class JuziconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juziconpro
        fields = (
            'title',
            'img_url',
            'tags',
            'intro',
            'content_list',
            'localImgPath'
        )
class JuzitagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juzitagtable
        fields = (
            # 最新
            'con_time',
            # 句子去重id
            'uuid',
            'tags',
            'intro',
            'content_list',
            'title',
            'img_url',
            'localImgPath',

        )

        # title = models.CharField(max_length=188)
        # content = models.TextField()
        # img_url = models.CharField(max_length=250)
        # localImg = models.CharField(max_length=250)
        # funny_num = models.CharField(max_length=20)
        # comment_num = models.CharField(max_length=20)
        # comment_list = models.TextField()
        # clsid = models.ForeignKey('ClsTable')