from django.conf.urls import url, include
from dtemplates import views

urlpatterns = [
    url(r'^djangoindex/$',views.djangoindex,name='djangoindex'),
]