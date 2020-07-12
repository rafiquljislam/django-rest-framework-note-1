from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Article
from .serializers import Article_Serializer
from rest_framework.decorators import  api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import  APIView
from rest_framework import  generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404




# class article_viewsets(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
#     serializer_class = Article_Serializer
#     queryset = Article.objects.all()



class article_viewsets(viewsets.ModelViewSet):
    serializer_class = Article_Serializer
    queryset = Article.objects.all()

