from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event, Guest
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


# Create your views here.
# 一个请求的主要处理逻辑
def hello(request):
    return render(request, "hello.html")


def login(request):
    """实现登录功能"""
    if request.method == "GET":
        # 返回登录页面
        return render(request, "index.html")
    else:
        # 处理登录请求
        my_username = request.POST.get("username")
        my_password = request.POST.get("password")

        if my_username == "" or my_password == "":
            return render(request, "index.html", {"hint": "username or password null!"})

        user = auth.authenticate(username=my_username, password=my_password)
        if user is not None:
            auth.login(request, user)
            response = HttpResponseRedirect("/manage")
            # response.set_cookie('user', my_username, 3600) # 添加浏览器 cookie
            request.session['user2'] = my_username  # 添加 session
            return response
        else:
            return render(request, "index.html", {"hint": "username or password error!"})


# 这个试图，它要校验用户有没有登录过？
@login_required
def manage(request):
    """发布会管理页面"""
    # cookie_user = request.COOKIES.get('user')  # 读取浏览器 cookie
    cookie_user = request.session.get('user2')
    event_list = Event.objects.all()
    return render(request, "event_mange.html", {
        "welcome_user": cookie_user, "events": event_list})


@login_required
def search_event(request):
    """发布会管理页面"""
    # cookie_user = request.COOKIES.get('user')  # 读取浏览器 cookie
    if request.method == "GET":
        event_name = request.GET.get("name", "")
        event_list = Event.objects.filter(name__contains=event_name)
        return render(request, "event_mange.html", {"events": event_list})
    else:
        response = HttpResponseRedirect("/manage")
        return response


@login_required
def guest(request):
    """嘉宾管理页面"""
    # cookie_user = request.COOKIES.get('user')  # 读取浏览器 cookie
    cookie_user = request.session.get('user2')
    page = request.GET.get("page", "")
    guest_list = Guest.objects.all()
    p = Paginator(guest_list, 3)
    try:
        guest_page = p.page(page)
    except PageNotAnInteger:
        # 如果页数不是整型, 取第一页.
        guest_page = p.page(1)
    except EmptyPage:
        # 如果页数超出查询范围，取最后一页
        guest_page = p.page(p.num_pages)

    return render(request, "guest_mange.html", {
        "welcome_user": cookie_user, "guests": guest_page})


@login_required
def sign_index(request, event_id):
    """嘉宾签到"""
    event = get_object_or_404(Event, id=event_id)
    if request.method == "GET":
        return render(request, "sign_index.html", {"event": event})
    else:
        phone = request.POST.get("phone", "")

        guest = Guest.objects.filter(phone=phone)
        if len(guest) == 0:
            return render(request, "sign_index.html", {
                "event": event, "hint": "手机号不存在！"})

        guest = Guest.objects.filter(event_id=event_id, phone=phone)
        if len(guest) == 0:
            return render(request, "sign_index.html", {
                "event": event, "hint": "该手机号没有参加本次发布会！"})

        guest = Guest.objects.get(event_id=event_id, phone=phone)
        print("签到状态", guest.sign)
        if guest.sign is False:
            guest.sign = True
            guest.save()
            return render(request, "sign_index.html", {
                "event": event, "hint": "签到成功！"})
        else:
            return render(request, "sign_index.html", {
                "event": event, "hint": "该手机号已签到！"})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")

# cookie / sessionid

# 存折：
# 银行卡： sessionID  aoseirtuopqwehorqfij1241


# 客户端（浏览器）   --- request --->   服务端（django服务, urls.py->views.py） 
# 客户端（浏览器）   <--- response --- 服务端（django服务）

# username = aaa & password = bbb

# django 的开发模型：MTV

# M : models 模型，数据库
# T : templates 模板，页面，HTML+js+css
# V : views 视图，请求的处理逻辑

# 学习的重点：
# 登录
# * get、post，传参 
# * cookie的使用
