from django.contrib import admin
from django.conf.urls import url, include
from brequest import views

urlpatterns = [
    # url(r'^auser/',views.index),
    # 总路由找子视图
    url(r'^(?P<year>\d+)/(?P<city>[a-zA-Z]+)$',views.login,name='login'),
]
