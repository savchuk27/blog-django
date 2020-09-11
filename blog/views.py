from django.shortcuts import render
from .models import News
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Главная страница блога'
    }
    return render(request,'blog/home.html',data)

# class ShowNewsView(ListView):
#     model = News
    # template_name = 'blog/home.html'
    # context_object_name = 'news'
    # ordering = ['-date']
    # paginate_by = 4