from django.urls import path, re_path
from . import views

app_name = 'tos'

urlpatterns = [
    path('',views.policy_list,name='policy-list'),
    path('<slug:post>/',views.policy_detail,name='policy-detail'),
]