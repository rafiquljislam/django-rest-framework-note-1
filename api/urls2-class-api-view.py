from django.urls import path
from .views import  articleAPIView, article_detail


urlpatterns = [
    path('api/', articleAPIView.as_view()),
    path('api/<int:id>/', article_detail.as_view()),
]
