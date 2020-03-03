
from django.conf.urls import url, include
from ccookie import views
from ccookie.views import my_decorator

urlpatterns = [
    # url(r'^auser/',views.index),
    # 总路由找子视图
    url(r'^cookie_msg/$',views.cookie_msg,name='cookie_msg'),
    url(r'^session_work/$',views.session_work,name='session_work'),
    # url(r'^index/$',my_decorator(views.LoginView.as_view()),name='index'),
    # url(r'^index/$',views.LoginView.as_view(),name='index'),
    url(r'^index/$',views.LoginView_Decorator_MiXin.as_view(),name='index'),
]