from django.shortcuts import render
from .models import News
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

news = [
    {
        'title': 'Первая запись',
        'text': 'Текст для первой записи',
        'date' : '30 апреля',
        'author' : 'Vitalii'
    },
    {
        'title': 'Вторая запись',
        'text': 'Текст для второй записи',
        'date' : '30 апреля',
        'author' : ''
    }
]

def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Главная страница блога'
    }
    return render(request,'blog/home.html',data)
