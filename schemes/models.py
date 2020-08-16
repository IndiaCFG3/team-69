from django.db import models

# NOTE
# Age, Location, Gender, Income, Number of people in family, Only Child Policy, 
# Only Girl Child Policy, Refugees, Caste, Religion, 
# Minorities, Languages, Military experience, Government Officials, Disability, MSme's, Daily wage workers

# Create your models here.
class Schemes(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = [
        (OTHER, 'Other'),
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    name = models.CharField(max_length=120)
    age = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=120,null=True, blank=True)
    income = models.BigIntegerField(null=True, blank=True)
    family_size = models.IntegerField(null=True, blank=True)
    only_child = models.BooleanField()
    only_girl_child = models.BooleanField()
    refugee = models.BooleanField()
    caste = models.CharField(max_length=120, null=True, blank=True)
    religion = models.CharField(max_length=120, null=True, blank=True)
    minorities = models.CharField(max_length=120, null=True, blank=True)
    language = models.CharField(max_length=120, null=True, blank=True)
    military_experience = models.BooleanField()
    government_officials = models.BooleanField()
    disability = models.BooleanField()
    msme = models.BooleanField()
    daily_wage_workers = models.BooleanField()
    scheme_url = models.URLField(null=True, blank=True)