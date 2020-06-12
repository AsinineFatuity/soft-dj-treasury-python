from mpesa import views as mpesa_views
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls import url
urlpatterns=[
url('',mpesa_views.homePage,name="blog"),
url('blog-single/',mpesa_views.singlePage,name="blog-single"),
url('index/',mpesa_views.indexPage,name="index"),
]