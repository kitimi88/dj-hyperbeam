import random
import string
from django.shortcuts import render, redirect
from apps.passwordgen.forms import PasswordGeneratorForm
from django.contrib import messages


def generate_password(request):
    form = PasswordGeneratorForm(request.POST)
    if form.is_valid():
        length = form.cleaned_data['length']
        complexity = int(form.cleaned_data['complexity'])
        characters = ''

        if complexity == 1:
            characters = string.ascii_letters
        elif complexity == 2:
            characters = string.ascii_letters + string.digits
        elif complexity == 3:
            characters = string.ascii_letters + string.digits + string.punctuation
        
        else:
            messages.error(request,'Invalid.',extra_tags='alert alert-success alert-dismissible fade show')
            return redirect('passwordgen:index')
        
        password = ''.join(random.choice(characters) for i in range(length))

        return render(request,'passwordgen/index.html',{'password':password,'form':form})
    
    else:
        form = PasswordGeneratorForm()
    return render(request,'passwordgen/index.html',{'form':form})