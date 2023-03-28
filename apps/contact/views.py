from django.shortcuts import render, redirect
from apps.contact.forms import ContactForm
from apps.contact.models import ContactUs
from django.core.mail import BadHeaderError
from django.core.mail import send_mail as sm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


def contact_us(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request,'Feedback received!',extra_tags='alert alert-success alert-dismissible fade show')
            return redirect('/')
    
    else:
        contact_form = ContactForm()

    context = {
        'contact_form':contact_form
    }
    
    return render(request,'contact/contact.html',context)