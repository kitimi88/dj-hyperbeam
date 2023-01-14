from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=50,label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    email = forms.CharField(max_length=30,label='',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    body = forms.CharField(max_length=250,min_length=5, label='',widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Comment
        fields = ('name', 'email','body')
