from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import UserRegisterForm, UserUpdateForm
from .models import User


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form
            user.email      = form.cleaned_data.get('email')
            user.save()
            messages.success(request, f'Your account has been created! You can login now.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/user_signup.html', {'form': form})

@login_required
def profileview(request):
    return render(request, 'user/profile.html')    

@login_required
def profileupdate(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, f'Account update successfully!')
            return redirect('profile')

    else:
        form = UserUpdateForm(instance=request.user)
    context = {
        'form': form,
    }

    return render(request, 'user/profile-update.html', context)
