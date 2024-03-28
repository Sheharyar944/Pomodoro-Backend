from django.db import models
from user.models import User

# Create your models here.
class Scheme(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = False)
    name = models.CharField(max_length=50)
    pomodoro = models.TextField(max_length=20)
    short_break = models.TextField(max_length=20)
    long_break = models.TextField(max_length=20)
    long_break_delay = models.TextField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']