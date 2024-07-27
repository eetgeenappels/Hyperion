from django.urls import path
from . import views

urlpatterns = [
    path('streaming/', views.generate_chat_message_streaming, name="textgen")
]
