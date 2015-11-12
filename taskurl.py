__author__ = 'mityagov_vi'
from django.conf.urls import url
from task import views

urlpatterns = [
    url(r'^$', views.tasklist.as_view()),
    url(r'^(?P<pk>[0-9]+)$', views.detailtasklist.as_view()),
    url(r'^search/(?P<search>[\w]+)$', views.snippet_search),
]
