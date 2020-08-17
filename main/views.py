from django.shortcuts import render, redirect
from schemes.models import Schemes
from volunteers.models import VolunteerMember
from members.models import Member

def index(request):
    context = {
    }
    return render(request, 'main/index.html', context)


def contact(request):
    context = {
    }
    return render(request, 'main/contact.html', context)


def user_view(request):
    return render(request, 'main/user_view.html')


def home(request):
    schemes = Schemes.objects.all()
    context = {
        "schemes" : schemes
    }
    return render(request, 'main/home.html', context)


def dashboard(request):
    if(request.user.role == "end_user"):
        return render(request, 'main/dashboard.html')
    elif(request.user.role == "volunteer"):
        member=Member.objects.all()
        context={
            "member" : member
        }
        print(member)
        return render(request, 'user/vol_dashboard.html', context)

