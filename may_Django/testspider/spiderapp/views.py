from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework import permissions


# Create your views here.
class QiushiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Qiushipro.objects.all()
    serializer_class = QiushiSerializer
    permission_classes = (permissions.IsAuthenticated,)


class QiushiList(generics.ListAPIView):
    queryset = Qiushipro.objects.all()
    serializer_class = QiushiSerializer
    permission_classes = (permissions.IsAuthenticated,)

#句子控
class juziconDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Juziconpro.objects.all()
    serializer_class = JuziconSerializer
    permission_classes = (permissions.IsAuthenticated,)


class juziconList(generics.ListAPIView):
    queryset = Juziconpro.objects.all()
    serializer_class = JuziconSerializer
    permission_classes = (permissions.IsAuthenticated,)

#句子标签
class juzitagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Juzitagtable.objects.all()
    serializer_class = JuzitagSerializer
    permission_classes = (permissions.IsAuthenticated,)


class juzitagList(generics.ListAPIView):
    queryset = Juzitagtable.objects.all()
    serializer_class = JuzitagSerializer
    permission_classes = (permissions.IsAuthenticated,)

def myapptest(request):
    return render(request,'myapp.html')
