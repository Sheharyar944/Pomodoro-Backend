from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from task.models import Task

# @receiver(pre_save, sender=Task)
# def create_task_update(sender, instance,  **kwargs):
#     try:
#         old_instance = sender.objects.get(pk=instance.pk)
#     except sender.DoesNotExist:
#         return
    
#     if instance.remaining_pomodoros < old_instance.remaining_pomodoros and instance.remaining_pomodoros>0:
#         Task.objects.create(category=instance.category,
#                             description=instance.description,
#                             assigned_pomodoros=1,
#                             remaining_pomodoros=0,
#                             user = instance.user)