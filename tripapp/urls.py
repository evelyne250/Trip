from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.signIn),
    url(r'^api/new/$', views.MerchList.as_view()),


]