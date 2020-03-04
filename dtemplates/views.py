from django.shortcuts import render,redirect

from django.http.response import HttpResponse,JsonResponse
import json
from datetime import date
# Create your views here.

def djangoindex(request):
	# return HttpResponse("操作模板哦")
	content = {
		"name":"老王",
		"age":30,
		"sons":["小花","小张","小刘"],
		"wife":{
			"name":"翠花"
		},
		"date_time": date(2020,2,3),
		"data":"<a href='http://www.baidu.com'>百度链接</a>"

	}
	return render(request,'son.html',context=content)
