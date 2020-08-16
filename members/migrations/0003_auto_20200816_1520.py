# Generated by Django 3.1 on 2020-08-16 09:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]