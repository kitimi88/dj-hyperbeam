from django.urls import path
# from . import views
from apps.blog import views
from . feeds import LatestPostsFeed


app_name = 'blog'

urlpatterns=[

    path('',views.post_list,name="post-list"),
    path('article/<slug:post>/',views.post_detail,name="post-detail"),
    path('comment/reply/', views.reply_page, name="reply"),
    path('tag/<slug:tag_slug>/',views.post_list, name='post_tag'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
]


