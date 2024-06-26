# Generated by Django 5.0.1 on 2024-03-15 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomodoro', '0006_pomodoro_settings_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pomodoro',
            name='long_break_duration',
            field=models.IntegerField(default=900),
        ),
        migrations.AlterField(
            model_name='pomodoro',
            name='pomodoro_duration',
            field=models.IntegerField(default=1500),
        ),
        migrations.AlterField(
            model_name='pomodoro',
            name='short_break_duration',
            field=models.IntegerField(default=300),
        ),
    ]
