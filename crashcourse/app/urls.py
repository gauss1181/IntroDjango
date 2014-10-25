from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_task/$', views.add_task, name='add_task'))
