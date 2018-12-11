#-*- coding:utf-8 -*-        
# @time  :18-12-3 上午11:23    
# @Author :董振兵                
# @File   :serializers
from .models import *
from rest_framework import serializers
class AnswerSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        depth = 1
class QuestionSerializers(serializers.HyperlinkedModelSerializer):
    # author_id = serializers.StringRelatedField(source='author_id.name')
    class Meta:
        model = Question
        fields = '__all__'
class AuthorSerializers(serializers.HyperlinkedModelSerializer):
    questions = QuestionSerializers(many=True)

    class Meta:
        model = Author
        fields = '__all__'
        # exclude = ('add_time',):  除去指定的某些字段

        # 我们可以在 extra_kwargs 设置中的 view_name 和 lookup_field
        # 来正确配置我们的 URL
        # view_name 和 urls.py 中的 name 参数相对应，表示使用哪个 url
        # lookup_field 表示用哪个字段来作为 url 的唯一识别标记
        # 本例中每个 question 的 url 是通过 id 来区分的，所以该字段用 id
        extra_kwargs ={
            # 'url': {'view_name':'question-detail','lookup_field': 'id',},
            # 'questions':{'view_name':'question-list','lookup_field':'id'},
        }


class TagsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'
class CommentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
