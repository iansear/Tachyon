from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^jobboard/$', views.jobboard, name='jobboard'),
    url(r'^(?P<job_id>[0-9]+)/$', views.jobdetails, name='details'),
]
