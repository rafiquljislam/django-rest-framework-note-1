from django.urls import path,include
from .views import  article_viewsets
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('article', article_viewsets, basename='api_article')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/<int:pk>/', include(router.urls)),
]
 