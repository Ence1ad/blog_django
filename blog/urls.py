from django.urls import path
from .views import PostByCategory, Home, get_post

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', PostByCategory.as_view(), name='category'),
    path('post/<str:slug>/', get_post, name='post'),
]


