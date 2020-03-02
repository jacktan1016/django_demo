from django.shortcuts import render
from django.http.response import HttpResponse
from django.urls.base import reverse

# Create your views here.

def login(request):
	print("路由的反向解析为:",reverse('brouter:login'))
	return HttpResponse("重新注册一个应用哦")