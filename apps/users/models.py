from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
# from django.utils import timezone
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from ckeditor.fields import RichTextField


def profile_avatar_path(instance, filename):
    return f"profile_uploads/{instance.user.username}/avatar/{filename}"

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    avatar = models.ImageField(default='default_avatar.png',upload_to=profile_avatar_path, blank=True, null=True)
    bio = models.TextField()


    def __str__(self):
        return str(self.user.username)
    
    def get_absolute_url(self):
        return reverse('accounts:profile-page', args=[self.user.username])
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        max_size = (448, 448)
        if img.height > max_size[0] or img.width > max_size[1]:
            img.thumbnail(max_size)
            img.save(self.avatar.path)
