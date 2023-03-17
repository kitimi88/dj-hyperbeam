from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from django.utils.text import slugify
import math


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )

    title = models.CharField(max_length=100,null=True,blank=True)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    image = models.ImageField(default='static/assets/defaults/default_post.png',upload_to='media/posts/images',blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    content = RichTextUploadingField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='draft')
    featured = models.BooleanField(default=False)

    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ('-publish',)

    
    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('blog:post-detail',args=[self.slug])

    def get_comments(self):
        return self.comments.filter(parent=None).filter(active=True)
        
    def whenpublished(self):
        now = timezone.now()
        diff = now - self.publish
        #seconds
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds
            if seconds == 1:
                return str() + ' Just now'
            else:
                return str(seconds) + ' seconds ago'
        #minutes
        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)
            if minutes == 1:
                return str() + ' about a minute ago'
            else:
                return str(minutes) + ' minutes ago'
        #hours
        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)
            if hours == 1:
                return str() + ' about an hour ago'
            else:
                return str(hours) + ' hours ago'
        
        #days
        if diff.days >= 1 and diff.days < 7:
            days = diff.days
            if days == 1:
                return str() + ' Yesterday'
            else:
                return str(days) + ' days ago'
        #WEEKS
        if diff.days >= 7 and diff.days < 30:
            weeks = math.floor(diff.days/7)
            if weeks == 1:
                return str() + ' about a week ago'
            else:
                return str(weeks) + ' weeks ago'

        #months
        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)
            if months == 1:
                return str() + ' about a month ago'
            else:
                return str(months) + ' months ago'

        #years
        if diff.days >= 365:
            years = math.floor(diff.days/365)
            if years == 1:
                return str() + ' about a year ago'
            else:
                return str(years) + ' years ago'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField()
    posted = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('updated',)
    
    def __str__(self):
        return self.body

    def get_comments(self):
        return Comment.objects.filter(parent=self).filter(active=True)
    
    def whenposted(self):
        now = timezone.now()
        diff = now - self.posted
        #seconds
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds
            if seconds == 1:
                return str() + ' Just now'
            else:
                return str(seconds) + ' seconds ago'
        #minutes
        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)
            if minutes == 1:
                return str() + ' about a minute ago'
            else:
                return str(minutes) + ' minutes ago'
        #hours
        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)
            if hours == 1:
                return str() + ' about an hour ago'
            else:
                return str(hours) + ' hours ago'
        
        #days
        if diff.days >= 1 and diff.days < 7:
            days = diff.days
            if days == 1:
                return str() + ' Yesterday'
            else:
                return str(days) + ' days ago'
        #WEEKS
        if diff.days >= 7 and diff.days <30:
            weeks = math.floor(diff.days/7)
            if weeks == 1:
                return str() + ' about a week ago'
            else:
                return str(weeks) + ' weeks ago'
        
        #months
        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)
            if months == 1:
                return str() + ' about a month ago'
            else:
                return str(months) +' months ago'

        #years
        if diff.days >= 365:
            years = math.floor(diff.days/365)
            if years == 1:
                return str() + ' about a year ago'
            else:
                return str(years) + ' years ago'  
    

# class Like(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    post = models.ForeignKey('Post',on_delete=models.CASCADE)
    