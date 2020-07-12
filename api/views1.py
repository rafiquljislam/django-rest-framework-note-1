from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from  rest_framework.parsers import JSONParser
from .models import Article
from .serializers import Article_Serializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = Article_Serializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        date = JSONParser().parse(request)
        serializer = Article_Serializer(data=date)

        if serializer.is_valid():
            serializer.save()
            return  JsonResponse(serializer.data,  status=201)
        return  JsonResponse(serializer.errors, status=400)

@csrf_exempt
def articla_detail(request, pk):
    try:
        article = Article.objects.get(id=pk)
    except Article.DoesNotExist:
        return  HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Article_Serializer(article)
        return  JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        date = JSONParser().parse(request)
        serializer = Article_Serializer(article, data=date)
        if serializer.is_valid():
            serializer.save()
            return  JsonResponse(serializer.data)
        return  JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        article.delete()
        return  HttpResponse(status=204)

