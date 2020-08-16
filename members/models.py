from django.db import models
from user.models import User


class Member(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    dob = models.DateField()
    income = models.IntegerField()
    family_size = models.IntegerField()
    gender = models.CharField(max_length=7)
    location = models.CharField(max_length=120)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="member")
