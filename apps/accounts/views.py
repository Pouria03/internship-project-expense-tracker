from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'ثبت‌نام با موفقیت انجام شد.')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'خوش آمدید {user.username}')
            return redirect('home')
        else:
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'خروج با موفقیت انجام شد.')
    return redirect('accounts:login')