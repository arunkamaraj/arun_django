from django.conf.urls import patterns, include, url
from arun_dj.models import Entry,Link,Category

urlpatterns =patterns('arun_dj.views',
   url(r'^$','category_list',name='category_index'),
   url(r'^(?P<slug>[-\w]+)/$','category_detail',name='category_detail'),

)

