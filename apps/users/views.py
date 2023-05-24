from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from apps.users.models import Profile
from django.contrib.auth.models import User
from apps.blog.models import Post


class AllUserProfile(ListView):
    model = Profile
    template_name = 'users/user_list.html'
    context_object_name = 'profiles'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        profiles = Profile.objects.all()
        context['all-users'] = profiles

        return context

def MyProfile(request,username):
    profile = User.objects.get(username=username)
    profile_details = Profile.objects.get(user=profile.id)
    user_post = Post.published.filter(author=profile.id).order_by('-pub_date')

    context = {
        'profile': profile,
        'profile_details': profile_details,
        'user_post':user_post
    }
    
    return render(request,'users/user_profile.html',context=context)
