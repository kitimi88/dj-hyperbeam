from django.urls import path, re_path
from apps.pages import views
from apps.pages.views import AboutPage

app_name = 'pages'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('about/',AboutPage.as_view(),name='about'),
    path('policy/',views.policy_list,name='policy-list'),
    path('policy/<slug:post>/',views.policy_detail,name='policy-detail'),
    
    #re_path(r'^.*\.*', views.pages, name='pages'),
]