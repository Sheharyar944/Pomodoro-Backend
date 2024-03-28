from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("pomodoro/", views.PomodoroSettingsView.as_view()),
    path("pomodoro/<int:user_id>/", views.PomodoroSettingsUpdateView.as_view()),
   
]

urlpatterns = format_suffix_patterns(urlpatterns)