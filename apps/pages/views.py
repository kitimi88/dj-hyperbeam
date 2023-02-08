from django.shortcuts import render,get_object_or_404, redirect
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.blog.models import Post
from apps.polls.models import Poll
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from taggit.models import Tag
from django.db.models import Q

from django.views.generic import TemplateView

# @login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('pages/index.html')
    return HttpResponse(html_template.render(context, request))

def post_list(request, tag_slug=None):
    posts = Post.published.all()
    latest_posts = Post.objects.order_by('-updated')[0:3]
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    query = request.GET.get("q")
    if query:
        posts=Post.published.filter(Q(title__icontains=query) | Q(tags__name__icontains=query)).distinct()
            
    
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
        'pages': page,
        'tag': tag
    }
        
    return render(request,'pages/index.html',context)

def poll_list(request):
    polls = Poll.objects.all()
    latest_polls = Poll.objects.order_by('-updated')[0:3]

    query = request.GET.get('q')
    if query:
        polls = Poll.objects.filter(Q(title__icontains=query)).distinct()

    paginator = Paginator(polls,6)
    page = request.GET.get('page')
    try:
        polls = paginator.page(page)
    except PageNotAnInteger:
        polls = paginator.page(1)
    except EmptyPage:
        polls = paginator.page(paginator.num_pages)

    context = {
        'polls':polls,
        'latest_polls':latest_polls
    }
    return render(request,'pages/index.html',context)
# @login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('pages/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('pages/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('pages/page-500.html')
        return HttpResponse(html_template.render(context, request))

class AboutPage(TemplateView):
    template_name = 'pages/about.html'
