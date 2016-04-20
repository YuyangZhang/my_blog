"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'article.views.home',name = 'home'),
    url(r'^post/(?P<id>\d+)/$', 'article.views.detail', name='detail'),
    url(r'^list/(?P<cat>\d+)/$', 'article.views.lists', name='lists'),
    url(r'^addArticle_form/$', 'article.views.addArticle_form', name='addArticle_form'),
    url(r'^addArticle/$', 'article.views.addArticle', name='addArticle'),
    url(r'^updateArticle_form/$', 'article.views.updateArticle_form', name='updateArticle_form'),
    url(r'^updateArticle_detail_form/(?P<id>\d+)/$', 'article.views.updateArticle_detail_form', name='updateArticle_detail_form'),
    url(r'^updateArticle/$', 'article.views.updateArticle', name='updateArticle'),
    url(r'^deleteArticle/(?P<article_id>\d+)/$', 'article.views.deleteArticle', name='deleteArticle'),
)
