# Generated by Django 3.1 on 2020-08-16 09:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='age',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
