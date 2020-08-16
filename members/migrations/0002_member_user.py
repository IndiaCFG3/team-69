# Generated by Django 3.1 on 2020-08-16 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='member', to='user.user'),
            preserve_default=False,
        ),
    ]
