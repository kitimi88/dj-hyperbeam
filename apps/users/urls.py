from django.urls import path
from .views import AllUserProfile
from . import views

app_name = 'users'

urlpatterns = [
    path('',AllUserProfile.as_view(),name='all-users'),
    path('<str:username>',views.MyProfile,name='profile-page'),
    
]