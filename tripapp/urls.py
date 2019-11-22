from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.signIn),
    url(r'^api/new/$', views.MerchList1.as_view()),
    url(r'^api/merch/$', views.MerchList.as_view())



]