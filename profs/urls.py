from django.conf.urls import url, include
from django.contrib import admin
from profs import views

urlpatterns = [
	url(r'profList/$', views.profList, name='profList'),
	url(r'profID/(\d+)/$', views.profView, name='profView'),
	url(r'profSearch/$', views.profSearch, name='search'),
]
