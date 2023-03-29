from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
import secrets

class Poll(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    description = RichTextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def user_can_vote(self):
        user_votes = self.vote_set.all()
        qs = user_votes.filter(poll=self)
        if qs.exist():
            return False
        return True

    @property
    def get_vote_count(self):
        return self.vote_set.count()

    def get_result_dict(self):
        res = []

        for choice in self.choice_set_all():
            d = {}

            alert_class = ['primary','secondary','sucess','danger','dark','warning','info']
            d['alert_class'] = secrets.choice(alert_class)
            d['text'] = choice.choice_text
            d['num_votes'] = choice.choice_text

            if not self.get_vote_count:
                d['percentage'] = 0
            else:
                d['percentage'] = (choice.get_vote_count / self.get_vote_count) * 100
            
            res.append(d)
        
        return res
    
    def __str__(self):
        return self.title


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
   
    
    @property
    def get_vote_count(self):
        return self.vote_set.count()

    def __str__(self):
        return f"{self.poll.title[:25]} - {self.choice_text[:25]}"


class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    email = models.EmailField(null=True,blank=True)
    
    def __str__(self):
        return f'{self.poll.title[:100]} - {self.choice.choice_text[:15]} {self.email}'