from django.shortcuts import render
from .models import Schemes
from members.models import Member

# NOTE
# Age, Location, Gender, Income, Number of people in family, Only Child Policy, 
# Only Girl Child Policy, Refugees, Caste, Religion, 
# Minorities, Languages, Military experience, Government Officials, Disability, MSme's, Daily wage workers
# gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
# name = models.CharField(max_length=120)
# age = models.IntegerField()
# location = models.CharField(max_length=120)
# income = models.BigIntegerField()
# family_size = models.IntegerField()
# only_child = models.BooleanField()
# only_girl_child = models.BooleanField()
# refugee = models.BooleanField()
# caste = models.CharField(max_length=120)
# religion = models.CharField(max_length=120)
# minorities = models.CharField(max_length=120)
# language = models.CharField(max_length=120)
# military_experience = models.BooleanField()
# government_officials = models.BooleanField()
# disability = models.BooleanField()
# msme = models.BooleanField()
# daily_wage_workers = models.BooleanField()
# scheme_url = models.URLField(null=True, blank=True)

# Create your views here.
def searchSchemePage(request):
    template_name = 'main/filter.html'
    queryset = Schemes.objects.all()
    values = { "object_list":queryset }
    return render(request, template_name, values)

def searchResultsView(request):
    template_name = 'main/filter.html'
    query = self.request.GET.get('result')
    object_list = Schemes.objects.filter(
        Q(age__icontains=query)|Q(location__icontains=query)|Q(gender__icontains=query)|Q(income__icontains=query)|
        Q(family_size__icontains=query)|Q(only_child__icontains=query)|Q(only_girl_child__icontains=query)|Q(refugee__icontains=query)|
        Q(caste__icontains=query)|Q(religion__icontains=query)|Q(minorities__icontains=query)|Q(language__icontains=query)|
        Q(military_experience__icontains=query)|Q(name__icontains=query)|Q(government_officials__icontains=query)|Q(disability__icontains=query)|
        Q(msme__icontains=query)|Q(daily_wage_workers__icontains=query)|Q(scheme_url__icontains=query)
    )
    values = {
        "object_list" : object_list
    }
    return render(request, template_name, values)

def appliedSchemes(request):
    context = {
        'scheme': Schemes.objects.filter(applied_schemes=request.user.member),
    }
    return render(request, 'main/applied-scheme.html', context)

