from django.urls import path

from news import views

urlpatterns = [
    path('', views.main, name='main'),  
    path('create-news', views.create_news, name='create_news'),  
]