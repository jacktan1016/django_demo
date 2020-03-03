from django.shortcuts import render,redirect

from django.http.response import HttpResponse,JsonResponse
import json

from django.urls.base import reverse
# Create your views here.

def login(request,city,year):
	print("year:",year)
	print("city:",city)
	return HttpResponse("这是带参数的request,格式为/2008/beijing")

def login_query(request):
	data = request.GET
	print(type(data))
	# 取值
	a = data.getlist('a')
	b = data.get('b')
	return HttpResponse("a的值为{},b的值为{}".format(a,b))

def login_form(request):
	data = request.POST # 获取的是POST属性，可以识别form提交的参数，前面的GET只能识别get路径中紧接着参数
	print(type(data))
	# 取值
	a = data.getlist('a')
	b = data.get('b')
	return HttpResponse("a的值为{},b的值为{}".format(a,b))

def login_not_form(request):
	data = request.body # 获取的是body属性,非form表单
	print(type(data))  #结果为二进制 byte
	# 先转换为字符串，再转换为字典
	str_data = data.decode('gbk')
	dicT_data = json.loads(str_data)
	print(dicT_data)
	return HttpResponse(dicT_data)

def login_meta(request):
	data = request.META # 获取的是请求头属性
	print(data)  # 值是一个字典，可以通过键值对获取
	print(request.method)
	print(request.path)
	return HttpResponse("获取请求头相关信息")

def response_msg(request):
	# return HttpResponse(content="响应信息",status=200)
	response = HttpResponse()
	response.content="响应对象设置响应内容"
	response.status_code =200
	return response

def jsonresponse(request):

	# 方法一:
	data = {"a":1,"b":2}
	# str_data = json.dumps(data)
	# return HttpResponse(str_data,content_type="application/json")
	# 方法二:
	# return JsonResponse(data)
	# 传数组
	data_1 = [data]
	return JsonResponse(data_1,safe=False)

def response_redirect(request):
	# return redirect('/auser/index')
	# return redirect(reverse('login_query'))
	return redirect('http://www.baidu.com')