from django.db import models
from django.utils import timezone

class ContactUs(models.Model):
    email = models.EmailField()
    message = models.TextField()
    #screenshot = models.ImageField(upload_to='media/feedback/screenshots',blank=True,null=True)

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'

