from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
"""
创建视图函数，也就是功能函数
1、接收请求对象
2、解析请求对象
3、model,templete
4、返回响应对象
"""

# 1、接收请求对象

def index(request):
	# 2、 解析去找路由
	#3先省略

	# 4、返回对象
	return HttpResponse("hello 这是我的第一次使用django项目")
	
