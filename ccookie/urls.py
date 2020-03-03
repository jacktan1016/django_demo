
from django.conf.urls import url, include
from ccookie import views

urlpatterns = [
    # url(r'^auser/',views.index),
    # 总路由找子视图
    url(r'^cookie_msg/$',views.cookie_msg,name='cookie_msg'),
    url(r'^session_work/$',views.session_work,name='session_work'),
]