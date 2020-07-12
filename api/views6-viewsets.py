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




class article_viewsets(viewsets.ViewSet):

    def list(self, request):
        articles = Article.objects.all()
        serializer = Article_Serializer(articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = Article_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,  status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = Article_Serializer(article)
        return Response(serializer.data)
        
    def update(self, request, pk=None):
        article = Article.objects.get(pk=pk)
        serializer = Article_Serializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






########################

# class UserViewSet(viewsets.ViewSet):
#     """
#     Example empty viewset demonstrating the standard
#     actions that will be handled by a router class.

#     If you're using format suffixes, make sure to also include
#     the `format=None` keyword argument for each action.
#     """

#     def list(self, request):
#         pass

#     def create(self, request):
#         pass

#     def retrieve(self, request, pk=None):
#         pass

#     def update(self, request, pk=None):
#         pass

#     def partial_update(self, request, pk=None):
#         pass

#     def destroy(self, request, pk=None):
#         pass

# ##################

