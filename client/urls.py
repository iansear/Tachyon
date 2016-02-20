from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^registerclient/(?P<company_id>[0-9]+)/$', views.registerclient, name='register'),
    url(r'^login/$', views.loginclient, name='login'),
    url(r'^placejob/$', views.placejob, name='placejob'),
    url(r'^viewstatus/$', views.viewstatus, name='viewstatus'),
    url(r'^viewhistory/$', views.viewhistory, name='viewhistory'),
]
