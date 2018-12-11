from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from viewTest.models import register
from django.shortcuts import redirect


# Create your views here.
# def index(request):
#
#     return HttpResponse('ok,.....')
def show_arg(request,id1):  #传过来的而是str

    return HttpResponse('参数是:%s'% id1)
def index(request):
    str1 = 'request.path : %s'%request.path
    str2 = 'request.encoding : %s'%request.encoding
    dic = {'str1':str1,'str2':str2}
    return render(request,'request.html',dic)
def show_method(request):
    a = request.GET['name']
    return HttpResponse(a)
def show_reqarg(request):
    if request.method == 'GET':
        a = request.GET.get('a') #获取请求参数a
        b = request.GET.get('b') #获取请求参数b
        c = request.GET.get('c') #获取请求参数c
        return render(request,'show_getarg.html',{'a':a,'b':b,'c':c})
    else:
        uname = request.POST.get('uname') #获取uname
        gender = request.POST.get('gender') #获取gender
        hobbys = request.POST.getlist('hobbys') #获取hobbys   获取的是列表!!!!!
        return render(request,'show_postarg.html',{'uname':uname,'gender':gender,'hobbys':hobbys})
#子类JsonRsponese
def json1(request):

    return render(request,'json1.html')
def json2(request):

    return JsonResponse({'h1':'hello','h2':'world'})
#用户登录验证
#用户登录
def login(request):

    return render(request,'login.html')
#验证登录 返回信息
def verfiy(request):
    # acc = request.POST.get('acc','无fuck说')
    # pwd = request.POST.get('pwd','无fuck说')
    acc = request.GET.get('acc', '无fuck说')
    pwd = request.GET.get('pwd', '无fuck说')
    user = register.objects.filter(account=acc)
    if user:
        if user[0].password == pwd:
            token = {
                'info':'登录成功'
            }

        else:
            token = {
                'info': '登录失败',
                'info1': pwd,
                'info2': user[0].password,

            }
    else:
        token = {
            'info': '用户不存在'
        }
    # token ={
    #     'info':a,
    #     'info1':p,
    # }

    return JsonResponse(token)

#重定向 到首页
def red1(request):
    return redirect('/viewTest/index/')

#设置cookie
def set_cke(request):
    r = HttpResponse('设置cookie')
    r.set_cookie('key1','hello')
    return r
#获取cookie
def get_cke(request):
    read = HttpResponse('读取cookie:<br/>')
    if 'key1' in request.COOKIES:    #!!!是request 对象的 COOKIES 方法
        read.write('<h1>'+ request.COOKIES['key1'] + '</h1>')
    return read
#获取session
def set_ses(request):
    request.session['key2'] = 'hellopython'
    return HttpResponse('设置session')
def get_ses(request):
    h1 = request.session.get('key2','无fuck说')
    return HttpResponse('获得session:<br/>%s'% h1)


