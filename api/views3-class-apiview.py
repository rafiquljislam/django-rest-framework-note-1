from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Article
from .serializers import Article_Serializer
from rest_framework.decorators import  api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import  APIView

class articleAPIView(APIView):

    def get(self, request):
        articles = Article.objects.all()
        serializer = Article_Serializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Article_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,  status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class article_detail(APIView):

    def get_object(self, id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        article = self.get_object(id)
        serializer = Article_Serializer(article)
        return  Response(serializer.data)

    def put(self, request, id):
        article = self.get_object(id)
        serializer = Article_Serializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return  Response(status=status.HTTP_204_NO_CONTENT)






