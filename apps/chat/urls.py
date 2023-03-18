from django.urls import path
from apps.chat.views import chat

app_name = 'chat'

urlpatterns = [
    path('',chat,name='chat'),
]