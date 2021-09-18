from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class Categories(models.TextChoices):
    TRAVEL = 'travel'
    TECH = 'tech'
    LIFE = 'life'
    SUSTAINABILITY = 'sustainability'

class BlogPosts(models.model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    category = models.CharField(max_length=50,choices=Categories.choices, default=Categories.LIFE)
    description = models.CharField(max_length=150)
    month= models.CharField(max_length=3)
    day= models.CharField(max_length=2)
    content = models.TextField()
    


