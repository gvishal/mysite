from django.shortcuts import render,get_object_or_404

from bookmarks.models import Link,Tags
# Create your views here.

def index(request):
  all_link_list = Link.objects.all()
  all_tag_list = Tags.objects.all()
  context = {'all_link_list' : all_link_list,'all_tag_list' : all_tag_list}
  return render(request,'bookmarks/index.html',context)

def link_detail(request,link_id):
  link = get_object_or_404(Link,pk=link_id)
  return render(request,'bookmarks/link.html',{'link':link})
  
def tag_detail(request,tag_id):
  tag = get_object_or_404(Tags,pk=tag_id)
  return render(request,'bookmarks/tag.html',{'tag':tag})
    

