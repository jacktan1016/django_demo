from django.contrib import admin
from django.conf.urls import url, include
from brequest import views

urlpatterns = [
    # url(r'^auser/',views.index),
    # 总路由找子视图
    url(r'^(?P<year>\d+)/(?P<city>[a-zA-Z]+)$',views.login,name='login'),
    url(r'^login_query/$',views.login_query,name='login_query'),
    url(r'^login_form/$',views.login_form,name='login_form'),
    url(r'^login_not_form/$',views.login_not_form,name='login_not_form'),
    url(r'^login_meta/$',views.login_meta,name='login_meta'),
    url(r'^response_msg/$',views.response_msg,name='response_msg'),
    url(r'^jsonresponse/$',views.jsonresponse,name='jsonresponse'),
    url(r'^response_redirect/$',views.response_redirect,name='response_redirect'),
]
