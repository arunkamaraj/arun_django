from django.conf.urls import patterns, include, url
from arun_dj import views
from arun_dj.models import Entry,Link,Category
from tagging.models import Tag
from django.views.generic.dates import *
from django.views.generic.list import *
from django.views.generic.detail import *

urlpatterns= patterns('',
    #-------------------------------it is for Entry moel based urls ------------------------------------------------------------------------
    #if u dint give ^$ then it always take this is the url to process 
    url(r'^$','arun_dj.views.entries_index'),

    #important thing is we have to enclose the both regular exp and followd function and P shoul be in capital letter....
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<days>\d{2})/(?P<slug>[-\w]+)/$','arun_dj.views.entry_detail',name='testing'),

    #ArchiveIdexView for listing out the latest object .. it list out latest 10 object 
    #It is defined as class class EntryArchiveIndexView
    url(r'^archive/$',views.EntryArchiveIndexView.as_view(model=Entry,date_field='pub_date'),name='archive_index'),

    #   url(r'/archive/$',ArchiveIndexView.as_view(model=Entry,date_field='pub_date'),name='archive_index'),
    url(r'^(?P<year>\d{4})/$',YearArchiveView.as_view(queryset = Entry.objects.all(),date_field='pub_date',allow_future=True,make_object_list = True),name='yeararchiv'),

    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',MonthArchiveView.as_view(queryset = Entry.objects.all(),date_field='pub_date',allow_future=True,template_name='arun_dj/arun_entry_archive_month.html'),name='month_archive'),

    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',DayArchiveView.as_view(queryset = Entry.objects.all(),date_field='pub_date',allow_future=True),name='dayarchive'),

    #--------------------------------it is for Link model based urls ------------------------------------------------------------------------

    #url testing 
    #url(r'^link/$','arun_dj.views.link_test'),

    # it dont have make object list only it have as latest
    url(r'^link/archive/$',views.ArchiveIndexView.as_view(model=Entry,date_field='pub_date'),name='archive_index'),

    #   url(r'/archive/$',ArchiveIndexView.as_view(model=Entry,date_field='pub_date'),name='archive_index'),
    url(r'^link/(?P<year>\d{4})/$',YearArchiveView.as_view(queryset = Entry.objects.all(),date_field='pub_date',allow_future=True,make_object_list = True,template_name='arun_dj/link_archive_year.html'),name='yeararchiv'),

    url(r'^link/(?P<year>\d{4})/(?P<month>\w{3})/$',MonthArchiveView.as_view(queryset = Entry.objects.all(),date_field='pub_date',allow_future=True,template_name='arun_dj/link_archive_month.html'),name='month_archive'),

    url(r'^link/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',DayArchiveView.as_view(queryset = Entry.objects.all(),date_field='pub_date',allow_future=True),name='dayarchive'),
   

    #important thing is we have to enclose the both regular exp and followd function and P shoul be in capital letter....
    url(r'^link/(?P<year>\d{4})/(?P<month>\w{3})/(?P<days>\d{2})/(?P<slug>[-\w]+)/$','arun_dj.views.entry_detail',name='testing_link '),   

)
#------------------------------------this is catogery models based url ------------------------------------------------------------------
urlpatterns +=patterns('arun_dj.views',
   url(r'^category/$','category_list',name='category_testing'),
   url(r'^category/(?P<slug>[-\w]+)/$','category_detail',name='category_detail'),

)
    #----------------------------------- this is category models with generic based url  droped ----------------------------------------------
#urlpatterns +=patterns('',
#    url(r'^category/$',ListView.as_view(model=Category),name='category_list'),
#    url(r'^category/(?P<slug>[-/w]+)/$',viwes.Category_ListView.as_view(slug='slug'),name='category_detail'),
#)
#---------------------------------------- this is for  tagging application --------------------------------------------------------------
#Refer tagging application 
urlpatterns +=patterns('',
    url('^tag/$',ListView.as_view(model=Tag),name='taglist'),
    url('^tag/entries/$','tagging.views.tagged_object_list',{'queryset_or_model':Entry,'tag':'kama', 'related_tags':True, 'allow_empty':True,'template_name':'arun_dj/entries_by_tag.html'}),
    url('^tag/links/$','tagging.views.tagged_object_list',{'queryset_or_model':Link,'template_name':'arun_dj/links_by_tag.html'}),
)


