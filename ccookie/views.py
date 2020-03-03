from django.shortcuts import render,redirect

from django.http.response import HttpResponse,JsonResponse
import json

from django.urls.base import reverse
from django.views.generic import View
from django.utils.decorators import method_decorator

# Create your views here.

class DecoratorMixin:
	@classmethod
	def as_view(cls,*args,**kwargs):
		# 这里是没有as_view()
		view = super().as_view(*args,**kwargs)
		view = my_decorator(view)
		return view

# 利用多继承的方法将View的as_view()方法给DecoratorMixin类里的方法，这是一种思想
class LoginView_Decorator_MiXin(DecoratorMixin,View):
	def get(self,get):
		return HttpResponse("类视图--DecoratorMixin--get方法")
	def post(self,post):
		return HttpResponse("类视图--DecoratorMixin--post方法")



#定义一个装饰器
def my_decorator(func):
	def wrapper(request,*args,**kwargs):
		print("装饰器----")
		return func(request,*args,**kwargs)
	return wrapper

# 定义装饰器第二种办法
# def my_decorator(func):
# 	def wrapper(self,request,*args,**kwargs):
# 		print("装饰器----")
# 		return func(self,request,*args,**kwargs)
# 	return wrapper

# class LoginView_self(View):
# 	@my_decorator
# 	def get(self,get):
# 		return HttpResponse("类视图--装饰器--get方法")
# 	def post(self,post):
# 		return HttpResponse("类视图--装饰器--post方法")

# 方法三
# @method_decorator(my_decorator,name='dispatch')
# class LoginView(View):
# 	def get(self,get):
# 		return HttpResponse("类视图--method_decorator--get方法")
# 	def post(self,post):
# 		return HttpResponse("类视图--method_decorator--post方法")

# class LoginView(View):
# 	def get(self,get):
# 		return HttpResponse("类视图----get方法")
# 	def post(self,post):
# 		return HttpResponse("类视图----post方法")


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
	# request.session.flush()

	return HttpResponse("session 的操作")

def index(request):
	return HttpResponse("index...")