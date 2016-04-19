from django.db import models

# Create your models here.
class Article(models.Model) :
    title = models.CharField(max_length = 100) 
    pplay = models.CharField(max_length = 1)
    category = models.CharField(max_length = 50, blank = True)  
    date_time = models.DateTimeField(auto_now_add = True)
    content = models.TextField(blank = True, null = True)  

    def __unicode__(self) :
        return self.title

    class Meta:
        ordering = ['-date_time']

class Category(models.Model):
    name = models.CharField(max_length = 10)
    pplay = models.CharField(max_length = 1)
    articles = models.CharField(max_length = 2000)
    def __unicode__(self) :
        return self.name

    class Meta:
        ordering = ['name']
