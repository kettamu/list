__author__ = 'mityagov_vi'
from django.conf.urls import url
from task import views

urlpatterns = [
    url(r'^$', views.snippet_list),
    url(r'^(?P<pk>[0-9]+)$', views.snippet_detail),
    url(r'^search/(?P<search>[\w]+)$', views.snippet_search),
]
