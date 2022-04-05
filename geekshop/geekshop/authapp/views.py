from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from basket.models import Basket


def login(request):

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        #     else:
        #         print('Юзер не активный')
        # else:
        #     print(form.errors)

    else:
       form = UserLoginForm()
    context = {
        'title': 'Gekshop | Авторизация',
        'form': form
    }
    return render(request, 'authapp/login.html', context)

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
                form.save()
                messages.success(request, 'Вы успешно зарегистрировались')
                return HttpResponseRedirect(reverse('authapp:login'))
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    context = {
        'title': 'Gekshop | Регистрация',
        'form': form
    }
    return render(request, 'authapp/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, 'Данные измененны')
            # return HttpResponseRedirect(reverse(('authapp:profile')))
        else:
            messages.set_level(request, messages.ERROR)
            messages.success((request, form.errors))
            # print(form.errors)

    user_select = request.user
    context = {
        'title': 'Geek | Профиль',
        'form': UserProfileForm(instance=user_select),
        'baskets': Basket.objects.filter(user=user_select)
    }

    return render(request, 'authapp/profile.html', context)


def logout(request):
    auth.logout(request)
    return render(request, 'mainapp/index.html')
