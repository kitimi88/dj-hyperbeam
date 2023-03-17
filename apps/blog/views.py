from django.shortcuts import render, get_object_or_404, redirect
from apps.blog.models import Post, Comment
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .forms import CommentForm
from taggit.models import Tag
from django.db.models import Count
from django.db.models import Q
from django.views.generic import View, ListView, DetailView
from django.contrib import messages
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django import template
from django.urls import reverse


def featured_post(request):
    featured_post = Post.objects.filter(featured=True)[0:3]
    
    context = {
        'featured_post':featured_post
    }

    # return render(request,'blog/post_list.html',context)
    return render(request,'blog/blog_index.html',context=context)
    

def post_list(request, tag_slug=None):
    posts = Post.published.all()
    #featured_post = Post.published.filter(featured=True).first()
    # latest_posts = Post.objects.order_by('-updated')
    latest_posts = Post.published.filter().order_by('-publish')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    query = request.GET.get("q")
    if query:
        posts = Post.published.filter(Q(title__icontains=query) | Q(tags__name__icontains=query)).distinct()
            
    
    paginator = Paginator(posts,6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'latest_posts': latest_posts,
        #'featured_post':featured_post,
        'pages': page,
        'tag': tag
    }
        
    return render(request,'blog/blog_index.html',context=context)



def post_detail(request, post):
    post = get_object_or_404(Post,slug=post,status='published')

    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            messages.success(request, 'Thanks for commenting!',extra_tags='alert alert-success alert-dismissible fade show')
            return redirect(post.get_absolute_url()+'#'+str(new_comment.id))
    else:
        comment_form = CommentForm()

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:6]

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'similar_posts':similar_posts
    }
    
    return render(request, 'blog/post_detail.html',context=context)


    
def reply_page(request):
    if request.method == "POST":

        form = CommentForm(request.POST)
        
        if form.is_valid():
            post_id = request.POST.get('post_id') 
            parent_id = request.POST.get('parent') 
            post_url = request.POST.get('post_url')

            print(post_id)
            print(parent_id)
            print(post_url)


            reply = form.save(commit=False)
    
            reply.post = Post(id=post_id)
            reply.parent = Comment(id=parent_id)
            reply.save()

            return redirect(post_url+'#'+str(reply.id))

    return redirect("/")

class SearchView(View):
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q','')
        search_result = Post.objects.filter(Q(title__icontains=q) | Q(tags__name__icontains=q)).distinct()

        context = {
            'search_result':search_result
        }
        return render(request,'pages/search.html',context=context)
