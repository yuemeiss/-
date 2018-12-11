from django.shortcuts import render

# Create your views here.
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