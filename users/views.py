from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserOurRegistration
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserOurRegistration(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} был создан, введите имя пользователя и пароль для авторизации')
            return redirect('auth')
    else:
        form = UserOurRegistration()
    return render(request,'users/registration.html',{'form': form, 'title': 'Регистарция пользователя'})

@login_required
def profile(request):
    return render(request, 'users/profile.html')