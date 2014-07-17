from django.conf.urls import patterns, url

from bookmarks import views

urlpatterns = patterns('',
  # ex: /bookmarks/
  url(r'^$', views.index, name='index'),
  # ex: /bookmarks/link/5
  url(r'^link/(?P<link_id>\d+)/$', views.link_detail, name='linkdetail'),
  # ex: /bookmarks/tag/5
  url(r'^tag/(?P<tag_id>\d+)/$', views.tag_detail, name='tagdetail'),
)
