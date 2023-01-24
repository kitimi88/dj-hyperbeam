from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import UserProfile
from django.contrib.auth.models import User

class UserProfileView(DetailView):
    model = UserProfile
    template_name = 'users/user_profile.html'
    context_object_name = 'profile'

def MyProfile(request,username):
    profile = User.objects.get(username=username)
    profile_details = UserProfile.objects.get(user = profile.id)
    
    context = {
        'profile': profile,
        'profile_details': profile_details
    }
    
    return render(request,'users/user_profile.html',context)

class UserProfileList(ListView):
    model = UserProfile
    template_name = 'users/user_list.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        profile = UserProfile.objects.all()
        context ['user-list'] = profile

        return context