from re import I
from django.db import models
from datetime import datetime
from django.utils.text import slugify
# Create your models here.

class Categories(models.TextChoices):
    DJANGO = 'django'
    CELERY = 'celery'
    POSTGRESQL = 'postgresql'
    SQL = 'sql'
    DOCKER = 'docker'
    PYTHON = 'python'
    REACTJS = 'reactjs'
    JAVASCRIPT = 'javascript'
    OTHER = 'other'

class BlogPost(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField()
    category = models.CharField(max_length=20,choices=Categories.choices, default=Categories.DJANGO)
    thumbnail = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    exercept = models.CharField(max_length=200)
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self,*args,**kwargs):
        original_slug = slugify(self.title)
        qs = BlogPost.objects.all().filter(slug__iexact = original_slug).count()
        count = 1 
        slug = original_slug
        while(qs):
            slug = original_slug + '-'+ str(count)
            count += 1
            qs = BlogPost.objects.all().filter(slug__iexact = slug).count()

        self.slug = slug
        
        if self.featured:
            try:
                temp = BlogPost.objects.get(featured = True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except BlogPost.DoesNotExist:
                pass

        return super(BlogPost,self).save(*args,**kwargs)
             
    def __str__(self):
        return self.title

    