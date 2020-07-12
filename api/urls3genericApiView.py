from django.urls import path
from .views import  genericApiView


urlpatterns = [
    path('api/<int:id>/', genericApiView.as_view()),
    path('api/', genericApiView.as_view()),
    # path('api/<int:id>/', article_detail.as_view()),
]
