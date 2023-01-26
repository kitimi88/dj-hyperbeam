from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactUs
from django.core.mail import BadHeaderError
from django.core.mail import send_mail as sm
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib import messages

# def contact_us(request):
#     contactdetails = ContactUs.objects.last()
#     template = 'contact/contact.html'

#     if request.method == 'POST':
#         contact_form = ContactForm(request.POST)
#         if contact_form.is_valid():
#             from_email = contact_form.cleaned_data['email']
#             message = contact_form.cleaned_data['message']

#             try:
#                 sm(from_email,message,)
            
#             except BadHeaderError:
#                 return HttpResponse('invalid header')
            
#             return redirect('contact:success')
    
#     else:
#         contact_form = ContactForm()

    
#     context = {
#         'contactdetails' : contactdetails,
#         'contact_form' : contact_form
#     }

#     return render(request,template,context)

# def success(request):
#     return HttpResponse('Thank you for your feedback.')

def contact_us(request):
    # contactdetails = ContactUs.objects.all()
    # template = 'contact/contact.html'

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request,'Feedback received!',extra_tags='alert alert-success alert-dismissible fade show')
            return redirect('/')
    
    else:
        contact_form = ContactForm()

    context = {
        # 'contactdetails':contactdetails,
        # 'template':template,
        'contact_form':contact_form
    }
    
    return render(request,'contact/contact.html',context)