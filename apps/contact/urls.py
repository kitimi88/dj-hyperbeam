from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('',views.contact_us,name='contact-us'),
  #  path('success/',views.success,name='success'),
]