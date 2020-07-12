from django.urls import path
from .views import  genericApiView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('api/<int:id>/', genericApiView.as_view()),
    path('api/', genericApiView.as_view()),
    path('login/', obtain_auth_token),
]
