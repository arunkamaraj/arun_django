from django.conf.urls import patterns, include, url
from arun_dj.models import Entry,Link,Category
from django.views.generic.dates import *
from arun_dj import views

urlpatterns=patterns('',
    #url testing 
    #url(r'^$','arun_dj.views.link_test'),

    # it dont have make object list only it have as latest
    url(r'^$',ArchiveIndexView.as_view(model=Link,date_field='pub_date'),name='link_index'),

    #   url(r'/archive/$',ArchiveIndexView.as_view(model=Entry,date_field='pub_date'),name='archive_index'),
    url(r'^(?P<year>\d{4})/$',YearArchiveView.as_view(queryset = Link.objects.all(),date_field='pub_date',allow_future=True,make_object_list = True,template_name='arun_dj/link_archive_year.html'),name='link_year_archiv'),

    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',MonthArchiveView.as_view(queryset = Link.objects.all(),date_field='pub_date',allow_future=True,template_name='arun_dj/link_archive_month.html'),name='link_month_archive'),

    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',DayArchiveView.as_view(queryset = Link.objects.all(),date_field='pub_date',allow_future=True),name='link_day_archive'),


    #important thing is we have to enclose the both regular exp and followd function and P shoul be in capital letter....
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<days>\d{2})/(?P<slug>[-\w]+)/$','arun_dj.views.link_detail',name='link_detail '),

)

