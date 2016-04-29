"""
URL прилодения gird_blog
"""
from django.conf.urls import url
from gird_blog.views import home, newslenta, articles, contacts, projects, detail

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^news/$', newslenta, name='news'),
    url(r'^articles/$', articles, name='articles'),
    url(r'^articles/sort/(?P<tag_id>[0-9]+)/$', articles, name='articles_sort'),
    url(r'^articles/detail/(?P<article_id>[0-9]+)/$', detail, name='detail'),
    url(r'^contacts/$', contacts, name='contacts'),
    url(r'^projects/$', projects, name='projects'),
]


