# Generated by Django 5.0.1 on 2024-03-21 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomodoro', '0009_alter_pomodoro_options_pomodoro_is_selected'),
    ]

    operations = [
        migrations.AddField(
            model_name='pomodoro',
            name='current_time',
            field=models.IntegerField(default=1500),
        ),
    ]
