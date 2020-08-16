from django.core.validators import MaxValueValidator
from django.db import models
from user.models import User


class Member(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    dob = models.DateField(verbose_name='Date Of Birth')
    income = models.PositiveIntegerField()
    family_size = models.PositiveIntegerField()
    GENDER = [
    	('MALE', 'Male'),
    	('FEMALE', 'Female'),
    	('WOULD NOT LIKE TO DISCLOSE', 'Would Not Like TO Disclose'),
    ]
    gender = models.CharField(choices=GENDER, default='WOULD NOT LIKE TO DISCLOSE', max_length=30)
    location = models.CharField(max_length=120)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="member")

