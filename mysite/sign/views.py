from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event, Guest

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
		print(type(my_username))
		print(type(my_password))
		
		if my_username == "" or my_password == "":
			return render(request, "index.html", {"hint": "用户名或密码为空！"})

		user = auth.authenticate(username=my_username, password=my_password)
		print("有没有这个用户", user)
		if user is not None:
			auth.login(request, user)
			response = HttpResponseRedirect("/manage")
			# response.set_cookie('user', my_username, 3600) # 添加浏览器 cookie
			request.session['user2'] = my_username  # 添加 session
			return response
		else:
			return render(request, "index.html", {"hint": "用户名密错误！"})


# 这个试图，它要校验用户有没有登录过？
@login_required
def manage(request):
	"""管理页面"""
	# cookie_user = request.COOKIES.get('user')  # 读取浏览器 cookie
	cookie_user = request.session.get('user2')
	event_list = Event.objects.all()
	print("---->", cookie_user)
	return render(request, "manage.html", {"welcome_user": cookie_user,
											"events": event_list})


def logout(request):
	auth.logout(request)
	return HttpResponseRedirect("/login")


# cookie / sessionid 

# 存折：
# 银行卡： sessionID  aoseirtuopqwehorqfij1241


# 客户端（浏览器）   --- request --->   服务端（django服务, urls.py->views.py） 
# 客户端（浏览器）   <--- response --- 服务端（django服务）

#username = aaa & password = bbb

# django 的开发模型：MTV

# M : models 模型，数据库
# T : templates 模板，页面，HTML+js+css
# V : views 视图，请求的处理逻辑

# 学习的重点：
# 登录
# * get、post，传参 
# * cookie的使用
