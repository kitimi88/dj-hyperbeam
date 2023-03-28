from django import forms
from apps.contact.models import ContactUs

class ContactForm(forms.ModelForm):
    email = forms.CharField(label='',max_length=50,min_length=10,required=True,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    message = forms.CharField(label='',max_length=250,min_length=5,required=True,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Feedback'}))

    class Meta:
        model = ContactUs
        fields = ('email','message',)