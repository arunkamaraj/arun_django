from django.shortcuts import render_to_response,get_object_or_404
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.detail import *
from arun_dj.models import Entry,Category,Link


def entries_index(request):
#	return render_to_response('arun_dj/entries_index.html',{'entry_list':Entry.objects.filter(status=Entry.LIVE_STATUS)})
	return render_to_response('arun_dj/entries_index.html',{'entry_list':Entry.live.all()})


def entry_detail(request,year,month,days,slug):
	import datetime,time
# 	forming the date value from string using Time module
	print 'insidetail'
	value=year+month+days
	std_time=time.strptime(value,"%Y%b%d")
	dt=datetime.date(*std_time[:3])	
	entry=get_object_or_404(Entry,pub_date__year=dt.year,pub_date__month=dt.month,pub_date__day=dt.day,slug=slug)
	print entry
	return render_to_response('arun_dj/entries_detail.html',{'object':entry})
#	return render_to_response('arun_dj/entries_detail.html',{'enrty':Entry.object.get(pub_date__year=dt.year,pub_date__month=dt.month,pub_date__day=dt.day,slug=slug)})

#       the most important thing is we no need to metionview for archive index view  refer urls.py

def category_list(request):
	return render_to_response('arun_dj/category_list.html',{'object_list':Category.objects.all()})

def category_detail(request,slug):
	category=get_object_or_404(Category,slug=slug)
	return render_to_response('arun_dj/category_detail.html',{'object_list':category.entry_set.filter(status=Entry.LIVE_STATUS),'category':category} )

def link_detail(request,year,month,days,slug):
	import datetime,time
#       forming the date value from string using Time module
        print 'insid link detail'
        value=year+month+days
        std_time=time.strptime(value,"%Y%b%d")
        dt=datetime.date(*std_time[:3])
	print dt,value,slug,dt.year,dt.month,dt.day 
        link=get_object_or_404(Link,pub_date__year=dt.year,pub_date__month=dt.month,pub_date__day=dt.day,slug=slug)
#	obj=Link.objects.all()
        return render_to_response('arun_dj/link_detail.html',{'object':link})

class EntryArchiveIndexView(ArchiveIndexView):
#	below line is equal to model=Entry we are passing the same vlaue thru url
#	queryset=Entry.objects.all() 
#	date_field='pub_date'
	make_object_list=False
	allow_future=True
        template_name='arun_dj/index_list.html'
	context_object_name='entry_list'
#------------------------------------------------ very tough bcz it is class basesd geneic view -----------------------------------------
#class Category_ListView(List_View):
#	category=get_object_or_404(Category,slug=slug)
#	return get(request,queryset=category.entry_set.all(),extra_context={'category':category})
#	def get_queryset(self):
#		category=get_object_or_404(Category,slug=self.slug)
#------------------------------------------------------------------------------------------------------------------------------------------
