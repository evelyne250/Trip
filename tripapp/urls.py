from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.welcome),
    url(r'^dashboard/$',views.dashboard),
    url(r'^dashboard/clients/$',views.dashboard1),
    url(r'^dashboard/drivers/$',views.dashboard2),
]