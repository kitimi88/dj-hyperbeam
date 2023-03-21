"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from apps.blog.sitemaps import PostSitemap
# from apps.blog import views as user_views

sitemaps = {
    'posts': PostSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('apps.blog.urls',namespace='blog')),
    path('hyperbeam/',include('apps.users.urls',namespace='users')),
    path('users/', include('django.contrib.auth.urls')),
    path('policy/',include('apps.tos.urls',namespace='tos')),
    path('contact-us/',include('apps.contact.urls',namespace='contact')),
    path('polls/',include('apps.polls.urls',namespace='polls')),
    path('chat/',include('apps.chat.urls',namespace='chat')),
    path('',include('apps.pages.urls',namespace='pages')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)