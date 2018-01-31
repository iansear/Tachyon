from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.loginuser, name='login'),
    url(r'^registercompany/$', views.registercompany, name='registercompany'),
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^canceljob/$', views.canceljob, name='canceljob'),
    url(r'^registercourier/$', views.registercourier, name='registercourier'),
    url(r'^assigncourier/$', views.assigncourier, name='assigncourier'),
    url(r'^listcouriers/$', views.listcouriers, name='listcouriers'),
    url(r'^(?P<courier_id>[0-9]+)/$', views.courierdetails, name='courierdetails'),
]
