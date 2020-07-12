from django.urls import path
from .views import  article_list, articla_detail


urlpatterns = [
    path('api/', article_list),
    path('api/<int:pk>/', articla_detail),
]
