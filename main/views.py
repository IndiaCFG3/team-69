from django.shortcuts import render
# Create your views here.


def index(request):
    context = {
    }
    return render(request, 'main/index.html', context)


def home(request):
    return render(request, 'main/home.html')


def dashboard(request):
    return render(request, 'main/dashboard.html')
