from  django import template
from arun_dj.models import Entry
from django.db.models import get_model

def do_latest_entry(parser,token):
	return LatestEntriesNode()

#it should be subclass of template.Node()
class LatestEntriesNode(template.Node):
#it should contain render() function
	def render(self,context):
#		[1,2,3,4][:2] is equal to a=[1,2,3,4] a[:2]
		context['latest_entry']=Entry.live.all()[:5]
		return ''

def do_latest_content(parser,token):
#	bits=token.content.split()
	bits=token.split_contents()
	if len(bits) != 5:
		raise template.TemplateSyntaxError("'get_latest_content' get 4 arguments get properly")
	model_arg=bits[1].split('.')
	if len(model_arg) != 2:
		raise template.TemplateSyntaxError("First argument should have 'applicationname.modelname'")
	model=get_model(*model_arg)
#	if nothing model got matched then it return none 
	return  LatestContentNode(model,bits[2],bits[4])	

class LatestContentNode(template.Node):
	def __init__(self,model,num,var):
		self.model=model
		self.num=int(num)
		self.var=var
	def render(self,context):
#		context[self.var]=self.model.objects.all()[:self.num]
#		the reason is for entry we rae using Live not a object as manager so we need to use default manager that is defined in model
		context[self.var]=self.model._default_manager.all()[:self.num]

	

register=template.Library()
register.tag('get_latest_entry',do_latest_entry)
register.tag('get_latest_content',do_latest_content)
