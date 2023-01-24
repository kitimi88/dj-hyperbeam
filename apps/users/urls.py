from django.urls import path
from .views import UserProfileView, UserProfileList
from . import views

app_name = 'users'

urlpatterns = [
    path('',UserProfileList.as_view(),name='user-list'),
    path('<str:username>',views.MyProfile,name='profile-page'),
]