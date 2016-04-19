from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article,Category
from datetime import datetime
from django.http import Http404
# Create your views here.
def home(request):
     post_list = Article.objects.all()
     return render(request, 'home.html', {'post_list' : post_list})

def detail(request, id):
     try:
        post = Article.objects.get(id=str(id))
     except Article.DoesNotExist:
        raise Http404
     return render(request, 'post.html', {'post' : post})
def lists(request, cat):
    if int(cat) == 1:
        try:
            res = Article.objects.filter(pplay=str(cat))
        except Article.DoesNotExist:
            raise Http404
        return render(request, 'bz.html', {'post_list' : res})
    elif int(cat) == 2:
        try:
            res = Article.objects.filter(pplay=str(cat))
        except Article.DoesNotExist:
            raise Http404
        return render(request, 'cd.html', {'post_list' : res})
    else:
    	post_list = Article.objects.all()
        return render(request, 'lists.html', {'post_list' : post_list})
