from django.db.models.signals import post_save, post_delete
from .serializers import PomodoroSerializer
from django.dispatch import receiver
from user.models import User
from .models import Pomodoro
from rest_framework.response import Response

@receiver(post_save, sender=User)
def create_user_pomodoro(sender, instance, created, **kwargs):
    if created:
        # Create Pomodoro instance for the newly registered user
        Pomodoro.objects.create(user=instance)

        Pomodoro.objects.create(
            user=instance,
            settings_name="personal",
            pomodoro_duration=30*60,
            short_break_duration=2*60,
            long_break_duration=25*60,
            is_selected=False
        )

        Pomodoro.objects.create(
            user=instance,
            settings_name="work",
            pomodoro_duration=50*60,
            short_break_duration=10*60,
            long_break_duration=20*60,
            long_break_delay=2,
            is_selected=False

        )

@receiver(post_save, sender=Pomodoro)
def update_other_pomodoros(sender, instance, created, **kwargs):
    if not created:
        user_id = instance.user_id
        other_pomodoros = Pomodoro.objects.filter(user_id=user_id).exclude(id=instance.id)
        # Update other pomodoros
        other_pomodoros.update(
                                is_pomodoro=instance.is_pomodoro,
                                pomodoro_count = instance.pomodoro_count,
                                is_long_break= instance.is_long_break,
                                  is_break=instance.is_break,
                                  auto_start_pomodoro=instance.auto_start_pomodoro,
                                  auto_start_break= instance.auto_start_break,
                                  is_selected = False,
                                  current_time= instance.current_time,
                                  is_disabled = instance.is_disabled,
                                  alarm_sound = instance.alarm_sound,
                                  ticking_sound = instance.ticking_sound,
                                  ticking_sound_break=instance.ticking_sound_break,
                                  one_min_notify = instance.one_min_notify,
                                  )


# @receiver(post_delete, sender=Pomodoro)
# def update_next_mode(sender, instance, **kwargs):
#     remaining_modes = Pomodoro.objects.filter(user=instance.user)
#     if remaining_modes.exists():
#         sorted_modes = remaining_modes.order_by('id')
#         next_mode = sorted_modes.first()
#         next_mode.is_selected = True
#         next_mode.save()
#         serializer = PomodoroSerializer(next_mode)
#         serialized_data = serializer.data
#         data = {
#             'message' : "Settings deleted successfully",
#             'mode': serialized_data
#         }
#         return Response(data)
#     else:
#         return Response({'message':'No Modes'})

        