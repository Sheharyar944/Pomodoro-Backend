from django.db import models
from user.models import User


# Create your models here.
class Task(models.Model):
    category = models.CharField(max_length=25, default="work")
    description = models.CharField(max_length=200)
    assigned_pomodoros = models.IntegerField(default=1)
    remaining_pomodoros = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.description