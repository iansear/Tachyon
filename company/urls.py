from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.loginuser, name='login'),
    url(r'^registercompany/$', views.registercompany, name='registercompany'),
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^jobboard/$', views.assigncourier, name='assigncourier'),
    url(r'^canceljob/$', views.canceljob, name='canceljob'),
    url(r'^registercourier/$', views.registercourier, name='registercourier'),
]
