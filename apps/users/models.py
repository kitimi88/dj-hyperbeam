from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.urls import reverse

class UserProfile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media/profile/avatar/',blank=True,default='static/assets/defaults/default_avatar.png')
    title = models.CharField(max_length=50,null=True)
    bio = models.TextField()

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __str__(self):
        return str(self.user.username)

    def get_absolute_url(self):
        return reverse('users:profile-page',args=[self.slug])