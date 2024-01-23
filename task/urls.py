from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'', views.TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls  