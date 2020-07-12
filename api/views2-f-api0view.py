from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from  rest_framework.parsers import JSONParser
from .models import Article
from .serializers import Article_Serializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import  api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def article_list(request):

    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = Article_Serializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Article_Serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,  status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def articla_detail(request, pk):
    try:
        article = Article.objects.get(id=pk)
    except Article.DoesNotExist:
        return  HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Article_Serializer(article)
        return  Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Article_Serializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return  Response(status=status.HTTP_204_NO_CONTENT)

