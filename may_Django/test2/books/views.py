from django.shortcuts import render
from .models import BookInfo,Practice
from django.db.models import F,Q

# Create your views here.
def index(request):
    # result = BookInfo.objects.all()
    # result = BookInfo.objects.filter(id__exact=2)
    #contains :是否包含
    # result = BookInfo.objects.filter(btitle__contains='射')
    # result = Practice.objects.all()
    #升序
    # result1 = Practice.objects.order_by()
    #降序
    # result1 = Practice.objects.order_by('-pSalary')
    # F 属性和属性的对比

    result = BookInfo.objects.filter(bread__gt=F('bcomment'))
    result1 = Practice.objects.filter(pPhone__isnull=True)

    # result = BookInfo.objects.get(pk=1)

    vv = {'list':result,'list1':result1}
    return render(request,'index1.html',vv)