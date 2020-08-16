from django.db import models
from members.models import Member
from user.models import User


class Volunteer(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=7)
    location = models.CharField(max_length=120)
    department = models.CharField(max_length=20, default="")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="volunteer")


class VolunteerMember(models.Model):
    volunteer = models.ForeignKey(
        Volunteer, on_delete=models.CASCADE, related_name="volunteer")
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name="member")
