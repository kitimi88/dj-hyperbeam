from django.urls import path, re_path
from apps.pages import views
from apps.pages.views import AboutPage

app_name = 'pages'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('about/',AboutPage.as_view(),name='about'),
    #re_path(r'^.*\.*', views.pages, name='pages'),
]