from django import forms
from .models import Vote

class ChoiceForm(forms.ModelForm):
   # choice_text = forms.CharField(label='',required=True,widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    email = forms.CharField(label='',max_length=50,min_length=10,required=True,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    class Meta:
        model = Vote
        fields = ('email',)