from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


@api_view(['GET'])
def api_root(request, format=None):
    return Response(
        {
            'question': reverse('question-list', request=request, format=format),
            'author': reverse('author-list', request=request, format=format)
        }
    )

# Create your views here.
#视图集
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers
    permission_classes = ()
    # 使用过滤器
    filter_backends = (DjangoFilterBackend,)
    # 定义需要使用过滤器的字段
    filter_fields = ('author_id',)
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    permission_classes = ()
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializers
    permission_classes = ()
    # 使用过滤器
    filter_backends = (DjangoFilterBackend,)
    # 定义需要使用过滤器的字段
    filter_fields = ('qid',)
class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializers
    permission_classes = ()
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = ()





def TemplateView(request):
    return render(request,'index1.html')
def practice(request):
    return render(request,'practice.html')
# class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializers
#     permission_classes = ()
#
#
# class QuestionList(generics.ListAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializers
#     permission_classes = ()
#回答
# class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
#
#     queryset = Answer.objects.all()
#     serializer_class = AnswerSerializers
#     # 可设置　根据查找的字段
#     lookup_field = 'qid'
#     permission_classes = (permissions.IsAuthenticated,)



# class AnswerList(generics.ListAPIView):
#     queryset = Answer.objects.all()
#
#     serializer_class = AnswerSerializers
    # 可设置　根据查找的字段
    # lookup_url_kwarg = 'qid'
    # permission_classes = (permissions.IsAuthenticated,)

    # def get_object(self):
    #
    #
    #     return queryset
# class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializers
#     permission_classes = ()
#
# class AuthorList(generics.ListAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializers
#     permission_classes = ()
#
