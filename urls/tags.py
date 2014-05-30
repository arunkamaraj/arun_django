from django.conf.urls import patterns, include, url
from tagging.models import Tag
from arun_dj.models import *
from django.views.generic.list import ListView

#Refer tagging application 
urlpatterns = patterns('',
    url('^$',ListView.as_view(model=Tag),name='tag_index'),
    url('^entries/$','tagging.views.tagged_object_list',{'queryset_or_model':Entry,'tag':'kama', 'related_tags':True, 'allow_empty':True,'template_name':'arun_dj/entries_by_tag.html'}),
    url('^links/$','tagging.views.tagged_object_list',{'queryset_or_model':Link,'template_name':'arun_dj/links_by_tag.html'}),
)


