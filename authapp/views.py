from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from authapp.models import ShopUser
from authapp.utils import send_verify_mail
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm


def login(request):
    login_form = ShopUserLoginForm(data=request.POST)

    next_url = request.GET.get('next', '')

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST.get('next'))
            return HttpResponseRedirect(reverse('index'))

    context = {
        'form': login_form,
        'title': 'Вход в систему',
        'next': next_url
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            user = register_form.save()
            if send_verify_mail(user):
                print("сообщение отправлено")
                return HttpResponseRedirect(reverse('auth:login'))
            else:
                print('ERROR: отправки почты')
                return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    context = {
        'form': register_form,
        'title': 'Регистрация',
    }

    return render(request, 'authapp/register.html', context)


def edit(request):
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('authapp:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    context = {
        'form': edit_form,
        'title': 'Редактирование профиля'
    }

    return render(request, 'authapp/edit.html', context)


def verify(request, email, activation_key):
    try:
        user = ShopUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user)
            return render(request, 'authapp/verification.html')
        else:
            print(f'error activation user: {user}')
            return render(request, 'authapp/verification.html')
    except Exception as err:
        print(f'error activation user: {err.args}')
        return HttpResponseRedirect(reverse('index'))

