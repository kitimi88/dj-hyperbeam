from django.shortcuts import render, get_object_or_404, redirect
from .models import Policy
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
#from .forms import CommentForm
from taggit.models import Tag
from django.db.models import Count
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django import template
from django.urls import reverse


class PostList(ListView):
    model = Policy
    # paginate_by= 6
    queryset=Policy.published.all()
    context_object_name = "posts"
    template_name = "tos/policy_list.html"

def policy_list(request, tag_slug=None):
    posts = Policy.published.all()

     # post tag
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    
    # search
    query = request.GET.get("q")
    if query:
        posts=Policy.published.filter(Q(title__icontains=query) | Q(tags__name__icontains=query)).distinct()
            
    
    paginator = Paginator(posts,6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
   
        
    return render(request,'tos/policy_list.html',{'posts':posts, page:'pages', 'tag':tag})


class PostDetail(DetailView):
    model = Policy
    context_object_name = "post"
    template_name = "tos/policy_detail.html"

def policy_detail(request, post):
    post=get_object_or_404(Policy,slug=post,status='published')
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Policy.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:6]
    
    return render(request, 'tos/policy_detail.html',{'post':post,'similar_posts':similar_posts})