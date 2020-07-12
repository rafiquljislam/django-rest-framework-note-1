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


class genericApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = Article_Serializer
    queryset = Article.objects.all()
    lookup_field = 'id'

    # authentication_classes = [ SessionAuthentication, BasicAuthentication ]
    authentication_classes = [ TokenAuthentication ]
    permission_classes = [ IsAuthenticated ]

    def get(self, request, id=None):

        if id:
            return  self.retrieve(request)
        else:
            return  self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id = None):
        return  self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

