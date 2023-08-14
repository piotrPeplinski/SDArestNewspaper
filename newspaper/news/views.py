from django.shortcuts import render, get_object_or_404
from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse
from .paginators import UserPaginator
from rest_framework import filters

# Create your views here.


class ListCreateArticles(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['-date']

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ListCreateUsers(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPaginator

    def get_permissions(self):
        return [permissions.IsAdminUser() if self.request.method == 'GET' else permissions.AllowAny()]

class APIRoot(APIView):
    def get(self, request, format=None):
        links = {
            'articles': reverse('articles',request=request),
            'users': reverse('users',request=request),
            'token': reverse('token',request=request),
        }
        return Response(links)