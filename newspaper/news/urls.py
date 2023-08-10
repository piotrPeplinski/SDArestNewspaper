from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('articles/', views.ListCreateArticles.as_view()),
    path('articles/<int:pk>/', views.ArticleDetail.as_view()),
    path('users/', views.ListCreateUsers.as_view()),
    path('get-token/', obtain_auth_token),

]

urlpatterns = format_suffix_patterns(urlpatterns)
