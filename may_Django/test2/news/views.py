from django.shortcuts import render
from .models import AreaInfo
# Create your views here.
def area(request,**val):
    # lone = AreaInfo.objects.all()
    # list = lone[0]
    if val == None:
        list = AreaInfo.area.filter(aparent__isnull=True)
    else:
        list = AreaInfo.area.filter(atitle__contains=val['username'])
    aa = {'list':list}
    return render(request,'area.html',aa)
