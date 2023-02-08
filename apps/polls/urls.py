from django.urls import path
from . import views
#from .views import PollVote


app_name = 'polls'

urlpatterns = [
    path('',views.poll_list,name='poll-list'),
    #path('<int:poll_id>/',PollVote.as_view,name='detail'),
    path('<int:poll_id>/', views.poll_detail, name='detail'),
    path('<int:poll_id>/results/', views.poll_vote, name='vote'),
  #  path('<int:poll_id>/', views.poll_result, name='result'),
]