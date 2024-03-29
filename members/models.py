from django.core.validators import MaxValueValidator
from django.db import models
from user.models import User
from schemes.models import Schemes

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
    schemes = models.ManyToManyField(Schemes, default=None, related_name='applied_schemes')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="member")

    def __str__(self):
        return self.user.email

class Document(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='document')
    aadhar_card = models.BooleanField(default=False)
    driving_license = models.BooleanField(default=False)
    voter_id = models.BooleanField(default=False)
    birth_certificate = models.BooleanField(default=False)
    pan_card = models.BooleanField(default=False)
    ration_card = models.BooleanField(default=False)

    def __str__(self):
        return self.member.user.email + '1'