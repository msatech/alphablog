from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from taggit.managers import TaggableManager
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import *

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    
    CategoryImage = models.ImageField(upload_to="category/img/", null=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    def __str__(self):
        return self.title
        
    def delete(self, *args, **kwargs):
        self.CategoryImage.delete()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        

        slug_name = slugify(self.title)
        new_slug = slug_name
        self.slug = new_slug 
        super(Category, self).save(*args, **kwargs)

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    
    content = CKEditor5Field('Text', config_name='extends', null=True, blank=True)
    BlogImage = models.ImageField(upload_to="blog/img/", null=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    category = models.ManyToManyField(Category)
    createdDate = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    metaDescription = models.TextField(null=True)

    def __str__(self):
        return self.title
        
    def delete(self, *args, **kwargs):
        self.BlogImage.delete()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        
        slug_name = slugify(self.title)
        new_slug = slug_name
        self.slug = new_slug 
        
        super(Blogs, self).save(*args, **kwargs)

class Comments(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True) 
    email = models.EmailField( max_length=100, null=True)  
    

class CommentReply(models.Model):
    previouscomment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    replycomment = models.TextField(null=True)
    blog = models.ForeignKey(Blogs, on_delete=models.SET_NULL, null=True)
    
class Keywords(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=200, null=True)
