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
def addArticle_form(request):
    return render(request, 'addArticle_form.html')
def updateArticle_form(request):
    post_list = Article.objects.all()
    return render(request, 'updateArticle_form.html', {'post_list' : post_list})
def updateArticle_detail_form(request, id):
     try:
        post = Article.objects.get(id=str(id))
     except Article.DoesNotExist:
        raise Http404
     return render(request, 'updateArticle_detail_form.html', {'post' : post})
def addArticle(request):
    if 'title' in request.GET and 'category' in request.GET and 'pplay' in request.GET:
        message = ''
        _title, _category, _pplay, _content = request.GET['title'], request.GET['category'], request.GET['pplay'], request.GET['content']
        try:
            newArticle = Article.objects.create(title = _title, category = _category, pplay = _pplay, content = _content)
            for tagName in _category.split(','):
                try:
                    tag = Category.objects.get(name = tagName)
                    tag.articles += ',' + str(newArticle.id)
                    message += "Updated category " + tagName +": " + tag.articles + '\n'
                    tag.save()
                except Category.DoesNotExist:
                    tag = Category.objects.create(name = tagName, pplay = _pplay, articles = str(newArticle.id))
                    message += "Added category " + tagName +": " + tag.articles + '\n'

            message += "Title:" + _title + ";\n" + "Category:" + _category + ";\n" + "Pplay:" + _pplay + ";\nID: " + str(newArticle.id) + " Added to db."
        except:
            message = 'Something wrong with db'
    else:
        message = 'Please fill in all blank.'
    return HttpResponse(message)
def updateArticle(request):
    if 'title' in request.GET and 'category' in request.GET and 'pplay' in request.GET:
        message = ''
        _id, _title, _category, _pplay, _content = request.GET['article_id'], request.GET['title'], request.GET['category'], request.GET['pplay'], request.GET['content']
        # try:
        curArticle = Article.objects.get(id=str(_id))
        if _title != curArticle.title:
            curArticle.title = _title
        if _content != curArticle.content:
            curArticle.content = _content
        if _pplay != curArticle.pplay:
            curArticle.pplay = _pplay
        if _category != curArticle.category:
            curTags = curArticle.category.split(',')
            newTags = _category.split(',')
            curArticle.category = _category
            addTags = [tag for tag in newTags if tag not in curTags]
            deleTags = [tag for tag in curTags if tag not in newTags]
            for tagName in addTags:
                try:
                    tag = Category.objects.get(name = tagName)
                    tag.articles += ',' + str(curArticle.id)
                    message += "Updated category " + tagName +": " + tag.articles + '\n'
                    tag.save()
                except Category.DoesNotExist:
                    tag = Category.objects.create(name = tagName, pplay = _pplay, articles = str(curArticle.id))
                    message += "Added category " + tagName +": " + tag.articles + '\n'
            for tagName in deleTags:
                tag = Category.objects.get(name = tagName)
                tagList = tag.articles.split(',')
                tagList.remove(str(curArticle.id))
                tag.articles = ','.join(tagList)
                if tag.articles == '':
                    tag.delete()
                    message += 'Removed ' + tagName + '\n'
                else:
                    message += "Updated category " + tagName +": " + tag.articles + '\n'
                    tag.save()
        curArticle.save()
        message += "Title:" + _title + ";\n" + "Category:" + _category + ";\n" + "Pplay:" + _pplay + ";\nID: " + str(curArticle.id) + " Added to db."
        # except:
        #     message = 'Something wrong with db'
    else:
        message = 'Please fill in all blank.'
    return HttpResponse(message)
def deleteArticle(request, article_id):
    try:
        message = " "
        dArticle = Article.objects.get(id = article_id)
        for tagName in dArticle.category.split(','):
            tag = Category.objects.get(name = tagName)
            tagList = tag.articles.split(',')
            tagList.remove(str(dArticle.id))
            tag.articles = ','.join(tagList)
            if tag.articles == '':
                tag.delete()
                message += 'Removed ' + tagName + '\n'
            else:
                message += "Updated category " + tagName +": " + tag.articles + '\n'
                tag.save()
        dArticle.delete()
    except Article.DoesNotExist:
        raise Http404
    return HttpResponse("Deleted " + dArticle.title + message)
