from django.shortcuts import render,redirect

from django.http.response import HttpResponse,JsonResponse
import json

from django.urls.base import reverse

# Create your views here.

def cookie_msg(request):
	# set_cookie
	response = HttpResponse('设置cookie')
	# HttpResponse.set_cookie('itcast','tanwen',max_age=30)  # max_age=30  时间为秒  静态方法
	response.set_cookie('itcast','tanwen') 

	# 获取COOKIE值
	cookie = request.COOKIES
	print(cookie)
	print(type(cookie))  # 字典
	print(cookie['itcast'])  # 取value值
	return response

def session_work(request):
	# 设置session
	# request.session['name'] = "tanwen"
	# # # # 获取session
	# print(request.session['name'])
	# 删除cookie指定键和值
	# del request.session['name']
	# 删除所有的键和值 request.session['name'].clear()
	# 删除整行
	request.session.flush()

	return HttpResponse("session 的操作")