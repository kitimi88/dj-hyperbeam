from django.shortcuts import render,get_object_or_404
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
from django.views.generic import TemplateView, ListView
from apps.pages.models import SitePolicy
from taggit.models import Tag
from django.db.models import Count
from django.db.models import Q
from django.views.generic import ListView, DetailView



class IndexView(ListView):
    def get(self, request, *args, **kwargs):
        latest_posts = Post.objects.order_by('-updated')[0:3]
        latest_polls = Poll.objects.order_by('-updated')[0:3]

        context = {
            'latest_posts':latest_posts,
            'latest_polls':latest_polls
        }
        return render(request,'pages/index.html',context=context)


class AboutPage(TemplateView):
    template_name = 'pages/about.html'


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

class PostList(ListView):
    model = SitePolicy
    # paginate_by= 6
    queryset=SitePolicy.published.all()
    context_object_name = "posts"
    template_name = "pages/policy_list.html"

def policy_list(request, tag_slug=None):
    posts = SitePolicy.published.all()

     # post tag
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    
    # search
    query = request.GET.get("q")
    if query:
        posts=SitePolicy.published.filter(Q(title__icontains=query) | Q(tags__name__icontains=query)).distinct()
            
    
    paginator = Paginator(posts,6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
   
        
    return render(request,'pages/policy_list.html',{'posts':posts, page:'pages', 'tag':tag})

class PostDetail(DetailView):
    model = SitePolicy
    context_object_name = "post"
    template_name = "pages/policy_detail.html"

def policy_detail(request, post):
    post=get_object_or_404(SitePolicy,slug=post,status='published')
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = SitePolicy.published.filter(tags__in=post_tags_ids).exclude(id=post.id) # type: ignore
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:6]
    
    return render(request, 'pages/policy_detail.html',{'post':post,'similar_posts':similar_posts})