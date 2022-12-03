from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('game/', views.game_view, name='game'),
]
