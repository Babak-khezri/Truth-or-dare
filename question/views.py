from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Question
# Create your views here.


def like_question(request, question_pk):
    print('helloooooooooooooooooo')
    if request.is_ajax():
        question = get_object_or_404(Question, pk=question_pk)
        question.likes += 1
        question.save()
        return JsonResponse({}, status=200)


def dislike_question(request, question_pk):
    if request.is_ajax():
        question = get_object_or_404(Question, pk=question_pk)
        question.likes += 1
        question.save()
        return JsonResponse({}, status=200)
