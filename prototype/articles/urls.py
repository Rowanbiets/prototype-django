from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('articles/', views.articles, name='articles'),
    path('articles/details/<int:id>', views.details, name='details'),   
]