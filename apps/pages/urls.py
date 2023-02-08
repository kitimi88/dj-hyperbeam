from django.urls import path, re_path
from apps.pages import views
from apps.pages.views import AboutPage

app_name = 'pages'

urlpatterns = [
    path('', views.post_list, name='index'),
    path('',views.poll_list,name='index'),
    path('about/',AboutPage.as_view(),name='about'),
    #re_path(r'^.*\.*', views.pages, name='pages'),
]