# Generated by Django 3.1 on 2020-08-16 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemes', '0003_auto_20200816_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schemes',
            name='location',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
