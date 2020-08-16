from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import CreateView
from .forms import UserRegisterForm, UserUpdateForm
from .models import User
from members.models import Member, Document

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.role = "end_user"
            user.email = form.cleaned_data.get('email')
            user.save()
            member = Member.objects.create(  user = user, 
                                    age  = form.cleaned_data.get('age'),
                                    name = form.cleaned_data.get('name'),
                                    dob  = form.cleaned_data.get('date_of_birth'),
                                    income = form.cleaned_data.get('income'),
                                    family_size = form.cleaned_data.get('family_size'),
                                    location = form.cleaned_data.get('location'),
                                )
            Document.objects.create(member=member)
            
            messages.success(request, f'Your account has been created! You can login now.')
            return redirect('/broadcast?id=28')
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
