from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('articles/', views.ListCreateArticles.as_view(), name='articles'),
    path('articles/<int:pk>/', views.ArticleDetail.as_view(),name='articleDetail'),
    path('users/', views.ListCreateUsers.as_view(), name='users'),
    path('get-token/', obtain_auth_token,name='token'),
    path('', views.APIRoot.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
