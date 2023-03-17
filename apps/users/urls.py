from django.urls import path
from apps.users.views import AllUserProfile
from . import views

app_name = 'users'

urlpatterns = [
    path('',AllUserProfile.as_view(),name='all-users'),
    path('admins/<str:username>/',views.MyProfile,name='profile-page'),
]