from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
import re

url = re.compile('^http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

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
    
def add_link(request):
  url_tag = request.POST['url_tag'].split(',')
  if url.match(url_tag[0]):
    link_url = url_tag[0]
    l = Link(url=link_url)
    l.save()
    tag_names = iter(url_tag)
    next(tag_names)
    for tag_name in tag_names:
      t = Tags(name=tag_name)
      t.save()
      l.tags.add(t)
  else:
    tag_name = url_tag[0]
    t = Tags.objects.filter(name = tag_name)
    if t:
      return redirect('/bookmarks/tag/%s' % t[0].id)
  return redirect('/bookmarks/')
