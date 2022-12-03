from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('game.urls')),
    path('question/',include('question.urls')),
]
