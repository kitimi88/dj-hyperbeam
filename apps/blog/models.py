from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from django.utils.text import slugify
import math
from PIL import Image

# return "user_{0}/{1}".format(instance.user.id, filename)


def post_image_path(instance, filename):
    return f"blog_uploads/{instance.author.username}/images/{filename}"

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='p')

class Post(models.Model):

    STATUS_CHOICES = (
        ("d","Draft"),
        ("p","Published"),
        ("w","Withdrawn")
    )

    title = models.CharField(max_length=100, null=True,blank=True)
    slug = models.SlugField(max_length=250, unique_for_date='pub_date')
    image = models.ImageField(default='default_post.png',upload_to=post_image_path, null=True, blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    content = RichTextUploadingField()
    pub_date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="d")
    featured = models.BooleanField(default=False)

    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ('-pub_date',)

    
    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('blog:post-detail',args=[self.slug])
    
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        
        if img.height > 1080 or img.width > 1920:
            new_img = (1080, 1920)
            img.thumbnail(new_img)
            img.save(self.image.path)


    def get_comments(self):
        return self.comments.filter(parent=None).filter(active=True) # type: ignore
        


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('-updated',)
    
    def __str__(self):
        return self.body

    def get_comments(self):
        return Comment.objects.filter(parent=self).filter(active=True)

    # def save(self, *args, **kwargs):
    #     super().save()

    

# class Like(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

# class Review(models.Model):
#     post = models.ForeignKey('Post',on_delete=models.CASCADE)
    