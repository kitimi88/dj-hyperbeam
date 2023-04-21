from django.urls import path
from . import views

app_name = 'passwordgen'

urlpatterns = [
    path('', views.generate_password, name='generate_password'),
]
