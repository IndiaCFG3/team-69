from django.shortcuts import render, redirect
from schemes.models import Schemes
from volunteers.models import VolunteerMember
from member.models import Member

def index(request):
    context = {
    }
    return render(request, 'main/index.html', context)


def contact(request):
    context = {
    }
    return render(request, 'main/contact.html', context)


def home(request):
    schemes = Schemes.objects.all()
    context = {
        schemes: schemes[0:5]
    }
    return render(request, 'main/home.html', context)


def dashboard(request):
    if(request.user.role == "end_user"):
        return render(request, 'main/dashboard.html')
    elif(request.user.role == "volunteer"):
        # volunteer_member = VolunteerMember.objects.filter(
        #     volunteer=request.user.volunteer).all()
        # print(volunteer_member)
        return render(request, 'user/vol_dashboard.html')

def appliedSchemes(request):
    context = {
        scheme: Schemes.objects.filter(applied_schemes=request.user.member),
    }
    return render(request, 'main/scheme.html', scheme)

