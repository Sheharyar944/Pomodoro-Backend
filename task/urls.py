from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
# from .views import UserTasksView

# router = routers.DefaultRouter()

# router.register(r'', views.TaskList, basename='task')

# urlpatterns = [
#     path('', include(router.urls)),
# ]

# urlpatterns += router.urls  

urlpatterns = [
    # path('', views.UserTasksView.as_view()),
    path('tasks/', views.TaskList.as_view()),
    path('createtasks/', views.CreateTaskView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)

