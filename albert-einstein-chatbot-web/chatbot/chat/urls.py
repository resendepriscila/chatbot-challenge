from django.urls import path
from .views import chatbot, question


urlpatterns = [
    path('chatbot/', chatbot),
    path('chatbot/<str:question>/', question),
]
