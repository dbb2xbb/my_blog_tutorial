from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404

# Create your views here.
def home(request):
	pl = Article.objects.all()
	context = {
		'post_list':pl
	}
	return render(request,'home.html',context)
def detail(request,id):
	try:
		post = Article.objects.get(id=str(id))
	except Article.DoesNotExsit:
		raise Http404
	
	return render(request,'post.html',{'post':post})


def test(request):
	return render(request,'test.html',{'current_time':datetime.now()})
