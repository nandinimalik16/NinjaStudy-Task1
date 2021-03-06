# Generated by Django 4.0.5 on 2022-06-25 19:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='experience',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student')], default='Student', max_length=50),
            preserve_default=False,
        ),
    ]
