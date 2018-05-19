from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def home(request):
	pl = Article.objects.all()
	paginator = Paginator(pl,2)
	page = request.GET.get('page')
	try:
		post_list = paginator.page(page)
	except PageNotAnInteger:
		post_list = paginator.page(1)
	except:
		post_list = paginator.paginator(paginator.num_pages)
	context = {
		'post_list':post_list
	}
	return render(request,'home.html',context)
def detail(request,id):
	try:
		post = Article.objects.get(id=str(id))
	except Article.DoesNotExsit:
		raise Http404
	
	return render(request,'post.html',{'post':post})
def archives(request):
	try:
		post_list = Article.objects.all()
	except:
		return Http404
	return render(request,'archives.html',{'post_list':post_list,'error':False})

def about_me(request):
	return render(request,'aboutme.html')

def cateClassify(request,category):
	try:
		post_list = Article.objects.filter(category = category)
	except:
		return Http404
	return render(request,'cateClassify.html',{'post_list':post_list})

def search(request):
	if 's' in request.GET:
		s = request.GET['s']
		if not s:
			return render(request,'home.html')
		else:
			post_list = Article.objects.filter(Q(title__contains = s)|Q(content__contains = s))
			if len(post_list) == 0:
				return render(request,'archives.html',{'post_list':post_list,'error':True})
			else:
				return render(request,'archives.html',{'post_list':post_list,'error':False})

	return redirect('/')

						

def test(request):
	return render(request,'test.html',{'current_time':datetime.now()})
