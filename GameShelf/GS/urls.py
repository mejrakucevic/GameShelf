from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('catalog/', views.catalog, name="catalog"),
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),
    


]
