from django.shortcuts import render
from .models import BookInfo


# Create your views here.
def index(request):

    s = BookInfo.objects.all()
    return render(request,'index1.html',{'s':s})