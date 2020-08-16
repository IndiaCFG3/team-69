from django.shortcuts import render
from schemes.models import Schemes
# Create your views here.


def index(request):
    context = {
    }
    return render(request, 'main/index.html', context)


def home(request):
    schemes = Schemes.objects.all()
    context = {
        schemes: schemes
    }
    return render(request, 'main/home.html', context)


def dashboard(request):
    return render(request, 'main/dashboard.html')
