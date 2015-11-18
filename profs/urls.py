from django.conf.urls import url, include
from django.contrib import admin
from profs import views

urlpatterns = [
	url(r'profList/$', views.profList, name='profList'),
	url(r'add_review/(\d+)/$', views.add_review, name='add_review'),
	url(r'profID/(\d+)/$', views.profView, name='profView'),
	url(r'profSearch/$', views.profSearch, name='search'),
	url(r'add_rating/(\d*)/$', views.add_rating, name='addRating'),
	url(r'add_professor/$', views.add_prof, name='addProfessor'),
]
