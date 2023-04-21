from django import forms

class PasswordGeneratorForm(forms.Form):
    length = forms.IntegerField(min_value=8,max_value=64,initial=12,label='')
    complexity = forms.ChoiceField(choices=((1, 'Weak'),(2, 'Medium'),(3, 'Strong'),),initial=2,label='')