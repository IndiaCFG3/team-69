# Generated by Django 3.1 on 2020-08-16 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schemes', '0004_auto_20200816_1904'),
        ('members', '0007_member_schemes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='schemes',
            field=models.ManyToManyField(default=None, related_name='applied_schemes', to='schemes.Schemes'),
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_card', models.BooleanField(default=False)),
                ('driving_license', models.BooleanField(default=False)),
                ('voter_id', models.BooleanField(default=False)),
                ('birth_certificate', models.BooleanField(default=False)),
                ('pan_card', models.BooleanField(default=False)),
                ('ration_card', models.BooleanField(default=False)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document', to='members.member')),
            ],
        ),
    ]