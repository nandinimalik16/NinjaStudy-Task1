# Generated by Django 4.0.5 on 2022-06-26 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_customuser_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=50)),
                ('task_description', models.TextField()),
                ('task_status', models.CharField(choices=[('Initiate', 'Initiate'), ('Pending', 'Pending'), ('Completed', 'Completed'), ('OnHold', 'OnHold')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TaskAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.task')),
            ],
        ),
    ]
