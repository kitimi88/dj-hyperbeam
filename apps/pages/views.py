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


