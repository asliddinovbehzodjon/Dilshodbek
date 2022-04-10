from django.urls import path
from .views import *
urlpatterns = [
    path('create/<str:file_name>/<int:chat_id>/<int:message_id>',new),
    path('get/<str:file_name>',Search.as_view())
]
