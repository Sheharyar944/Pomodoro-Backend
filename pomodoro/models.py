from django.db import models
from user.models import User
from task.models import Task

# Create your models here.
class Pomodoro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = False)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null = True, blank = True)
    settings_name = models.CharField(max_length=50, default="classic")
    pomodoro_duration = models.IntegerField(default=25*60)
    short_break_duration = models.IntegerField(default=5*60)
    long_break_duration = models.IntegerField(default=15*60)
    long_break_delay = models.IntegerField(default=4)
    is_pomodoro = models.BooleanField(default=True)
    pomodoro_count = models.IntegerField(default=0)
    is_long_break = models.BooleanField(default=False)
    is_break = models.BooleanField(default=False)
    daily_goal = models.IntegerField(default=1)
    auto_start_pomodoro = models.BooleanField(default=False)
    auto_start_break = models.BooleanField(default=False)
    is_selected = models.BooleanField(default=True)
    current_time = models.IntegerField(default=25*60)
    is_disabled = models.BooleanField(default=True)
    alarm_sound = models.BooleanField(default=True)
    ticking_sound = models.BooleanField(default=False)
    ticking_sound_break = models.BooleanField(default=False)
    one_min_notify = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']