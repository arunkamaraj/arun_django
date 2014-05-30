from django.conf.urls import patterns, include, url
from arun_dj.models import Entry,Link,Category
from arun_dj  import views
from django.views.generic.dates import *

urlpatterns=patterns('',
    #if u dint give ^$ then it always take this is the url to process 
    url(r'^$','arun_dj.views.entries_index',name='entry_index'),

    #important thing is we have to enclose the both regular exp and followd function and P shoul be in capital letter....
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<days>\d{2})/(?P<slug>[-\w]+)/$','arun_dj.views.entry_detail',name='entry_detail'),

    #ArchiveIdexView for listing out the latest object .. it list out latest 10 object 
    #It is defined as class class EntryArchiveIndexView
    url(r'^archive/$',views.EntryArchiveIndexView.as_view(model=Entry,date_field='pub_date'),name='archive_index'),

    #   url(r'/archive/$',ArchiveIndexView.as_view(model=Entry,date_field='pub_date'),name='archive_index'),
    url(r'^(?P<year>\d{4})/$',YearArchiveView.as_view(queryset = Entry.live.all(),date_field='pub_date',allow_future=True,make_object_list = True),name='year_archive'),

    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',MonthArchiveView.as_view(queryset = Entry.live.all(),date_field='pub_date',allow_future=True,template_name='arun_dj/entry_archive_month.html'),name='month_archive'),

    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',DayArchiveView.as_view(queryset = Entry.live.all(),date_field='pub_date',allow_future=True),name='day_archive'),

)
