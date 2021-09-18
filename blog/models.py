from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class Categories(models.TextChoices):
    TRAVEL = 'travel'
    TECH = 'tech'
    LIFE = 'life'
    SUSTAINABILITY = 'sustainability'

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField() #unique identifier
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    category = models.CharField(max_length=50,choices=Categories.choices, default=Categories.LIFE)
    description = models.CharField(max_length=150) #excerpt
    month= models.CharField(max_length=3)
    day= models.CharField(max_length=2)
    content = models.TextField() #inheriting from django summernote
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now,blank=True)
    
    #saving posts
    def save(self,*args,**kwargs):
        original_slug = slugify(self.title) #slug = title-like-this
        queryset = BlogPost.objects.all().filter(slug__iexact=original_slug).count() #counts slugs that match the original slug

        count = 1 #will be used for indexing the urls
        slug = original_slug #sets slug to slugified title

        #checks if posts are unique
        while(queryset):
            slug = original_slug + '-' + str(count)
            count +=1
            queryset=BlogPost.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        if self.featured:
            try:
                temp = BlogPost.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except BlogPost.DoesNotExist:
                pass
        
        super(BlogPost,self).save(*args,**kwargs)

    def __str__(self):
        return self.title