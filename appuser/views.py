import json

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import happybase

# Create your views here.
from django.views.decorators.cache import cache_page

from appuser.models import Zcareer, User

@cache_page(timeout=600,key_prefix='hbase')#缓存存入redis
def menu(request):
    # 展示 效果页面
    print('menu',request.META.get('HTTP_USER_AGENT'))
    # if 'py' in request.META.get('HTTP_USER_AGENT'):
    #     return HttpResponse('404 Not Found -----Got You Spider')
    if request.session.get('name'):
        connection = happybase.Connection(host="192.168.43.188", port=9090)
        connection.open()
        table = connection.table('crawler:t_zhilian')
        num = request.GET.get('num')
        name=request.GET.get('id')
        if not num:
            num = 1
        x="RowFilter(=,'regexstring:\.*"+name+"\.*')"
        print(x,num,name)
        a=table.scan(filter=x)
        l = []
        for i in a:
            # 将列表中的字典 转码 更换格式后传给列表l 传送给模板，进行解析
            dict1={}
            for j, k in i[1].items():
                try:
                    dict1.update({j.decode('utf-8').split(':')[1]: k.decode('utf-8').strip()})
                except Exception as a:
                    print(a)
                    pass
            if len(dict1['job'])>10:
                l.append(dict1)
        print(len(l),l)
        page = Paginator(object_list=l, per_page=10).page(num)
        return render(request,'main/menu.html',{'page':page,'name':name})
    else:
        return redirect('user:login')
def ajax(request):
    n=request.POST.get('forname')
    if User.objects.filter(username=n):
        return HttpResponse('用戶名存在')
    else:
        return HttpResponse('用戶名不存在')
# def ajax_fuzzy(request):
#     # ajax 模糊查询 展示
#     name=request.GET.get('name')
#     connection = happybase.Connection(host="192.168.43.188", port=9090)
#     connection.open()
#     table = connection.table('crawler:t_zhilian')
#     x = "RowFilter(=,'regexstring:\.*" + name + "\.*')"
#     print(x,name)
#     a = table.scan(filter=x)
#     l = []
#     for i in a:
#         # 将列表中的字典 转码 更换格式后传给列表l 传送给模板，进行解析
#         dict1 = {}
#         for j, k in i[1].items():
#             try:
#                 dict1.update({j.decode('utf-8').split(':')[1]: k.decode('utf-8').strip()})
#             except Exception as a:
#                 print(a)
#                 pass
#         if len(dict1['job']) > 10:
#             l.append(dict1)
#     print(len(l), l)
#
#     return JsonResponse(l,safe=False)
def index(request):
    # 主页面
    # request.META['HTTP_USER_AGENT']
    if 'py' in request.META.get('HTTP_USER_AGENT'):
        return HttpResponse('404 Not Found -----Got You Spider')
    return render(request,'main/main_port.html')
@cache_page(timeout=600,key_prefix='mysql')
def introduce(request):
    # 主页面中的 内部页面，展示页面
    print('in introduce')
    if request.session.get('name'):
        amount = Zcareer.objects.all()
    else:
        amount=Zcareer.objects.filter(pk__lte=50)

    num = request.GET.get('num')

    if not num:
        num = 1
    page = Paginator(object_list=amount, per_page=10).page(num)


    return render(request,'main/introduce.html', {'page': page, 'amount': amount})

def login(request):
    # 返回登录页面
    print('登录界面')
    # 如果密码输入错误，返回提示信息
    error=request.session.get('error')
    if not error:
        error=''
    else:
        del request.session['error']
    return render(request,'user/login.html',{'error':error})

def login_logic(request):
    # 判断登录逻辑，进行session存入，跳转到查询页面。
    print('进入登录逻辑logic')
    name=request.POST.get('userid')
    password=request.POST.get('psw')
    print(name,password)
    if User.objects.filter(username=name) and User.objects.filter(password=password):

        request.session['name']=name

        return redirect('main')
    else:
        request.session['error']='请检查用户名与密码'
        return redirect('user:login')

def regist(request):
    # 返回注册页面
    print('regist')
    return  render(request,'user/register.html')


def regist_logic(request):
    # 注册页面，注册成功后，跳转登录页面
    # print(request.META)
    # m=json.loads(request.META)
    print('注册逻辑')

    name=request.POST.get('userid')
    tel=request.POST.get('usrtel')
    email=request.POST.get('email')
    psw=request.POST.get('psw')
    print(name,tel,email,psw)
    return redirect('user:login')



