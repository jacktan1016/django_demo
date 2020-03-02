from django.contrib import admin
from brouter import views
from django.conf.urls import url, include

urlpatterns = [
    # url(r'^auser/',views.index),
    # 总路由找子视图
    url(r'^login/$',views.login,name='login'),
]
