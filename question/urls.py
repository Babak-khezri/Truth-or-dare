from django.urls import path
from . import views

app_name = 'question'

urlpatterns = [
    path('like_question/<int:question_pk>', views.like_question, name='like_question'),
    path('dislike_question/<int:question_pk>', views.dislike_question, name='dislike_question'),
]
