from unicodedata import category
from django.shortcuts import render

from question.models import Question
from random import choice
# Create your views here.


def home_view(request):
    # get_question()
    return render(request, 'game/home.html')


def get_question():
    with open('game/text.txt') as f:
        data = f.read().splitlines()
        for line in data:
            line = line.split('.')[1]
            Question.objects.create(text=line, category='d')
            print(line)


def start_game(request):
    return render(request, 'game/start_game.html')


def game_view(request):
    if request.method == 'GET':
        questions = []
        allow_rude = request.GET.get('allow_rude')
        if 'Dare' in request.GET:
            questions = Question.objects.filter(category='d')
        elif 'Truth' in request.GET:
            questions = Question.objects.filter(category='t')

        if questions:
            question = choice(questions)
            return render(request, 'game/game.html', {'question': question})
    return render(request, 'game/game.html')
