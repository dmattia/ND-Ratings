from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # user auth views
    #url(r'^accounts/', include('userprofile.urls')),
    url(r'^accounts/login/$', 'profRate.views.login'),
    url(r'^accounts/auth/$', 'profRate.views.auth_view'),
    url(r'^accounts/logout/$', 'profRate.views.logout'),
    url(r'^accounts/loggedin/$', 'profRate.views.loggedin'),
    url(r'^accounts/invalid/$', 'profRate.views.invalid_login'),
    # user registration
    url(r'^accounts/register/$', 'profRate.views.register_user'),
    url(r'^accounts/register_success/$', 'profRate.views.register_success'),
    url(r'^accounts/register_failure/$', 'profRate.views.register_failure'),
]
