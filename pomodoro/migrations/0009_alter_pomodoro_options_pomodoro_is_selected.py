# Generated by Django 5.0.1 on 2024-03-15 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomodoro', '0008_alter_pomodoro_pomodoro_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pomodoro',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='pomodoro',
            name='is_selected',
            field=models.BooleanField(default=True),
        ),
    ]
