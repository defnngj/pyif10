from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# 一个请求的主要处理逻辑
def hello(request):
	return render(request, "hello.html")


# django 的开发模型：MTV

# M : models 模型，数据库
# T : templates 模板，页面，HTML+js+css
# V : views 视图，请求的处理逻辑