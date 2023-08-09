from django.shortcuts import render, get_object_or_404
from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from django.contrib.auth.models import User


# Create your views here.

class ListCreateArticles(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ListCreateUsers(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer