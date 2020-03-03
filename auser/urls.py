from django.conf.urls import url
from auser import views

urlpatterns = [
    # 总路由找子应用
    url(r'^index/$',views.index),
    
]