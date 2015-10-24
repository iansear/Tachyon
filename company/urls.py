from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.loginuser, name='login'),
    url(r'^registercompany/$', views.registercompany, name='registercompany'),
    url(r'^admin/$', views.admin, name='admin'),
]
