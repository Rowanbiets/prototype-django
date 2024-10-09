from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 
from .views import user_activity_timeline

urlpatterns = [
    path('', views.main, name='main'),
    path('articles/', views.articles, name='articles'),
    path('articles/details/<int:id>', views.details, name='details'),
    
    # Login en Logout URLs
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    
    # CRUD voor artikelen
    path('articles/add/', views.article_add, name='article_add'),
    path('articles/edit/<int:id>/', views.article_edit, name='article_edit'),
    path('articles/delete/<int:id>/', views.article_delete, name='article_delete'),
    
    # Likes 
    path('articles/like/<int:id>/', views.like_article, name='like_article'),
    
    # tijdlijn
    path('timeline/', views.user_activity_timeline, name='timeline'),
   
    # ZoekFunctie
    path('search/', views.search_articles, name='search_articles'),
    
    # Statistieken
    path('statistics/', views.user_statistics, name='user_statistics'),
    
]
