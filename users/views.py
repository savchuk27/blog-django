from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm,
from django.contrib import messages
from .forms import UserOurRegistration, ProfileImage,UserUpdateForm
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
    if request.method == 'POST':
        img_profile = ProfileImage(request.POST, request.FILES, instance=request.user.profile)
        update_user = UserUpdateForm(request.POST,instance=request.user)
        if img_profile.is_valid() and update_user.is_valid() :
            update_user.save()
            img_profile.save()
            messages.success(request,f'Ваш аккаунт был успешно обновлен')
            return redirect('profile')
    else:
        img_profile = ProfileImage(instance=request.user.profile)
        update_user = UserUpdateForm(instance=request.user)

    data = {
        'img_profile' : img_profile,
        'update_user' : update_user
    }
    return render(request, 'users/profile.html', data)

# @login_required
# def profile(request):
#     img_profile = ProfileImage()
#     update_user = UserUpdateForm()
#     data = {
#             'img_profile' : img_profile,
#             'update_user' : update_user}
#     return render(request, 'users/profile.html',data)
