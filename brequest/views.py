from django.shortcuts import render

from django.http.response import HttpResponse
# Create your views here.

def login(request,city,year):
	print("year:",year)
	print("city:",city)
	return HttpResponse("这是带参数的request,格式为/2008/beijing")

