from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers
from .views import LoginView


router = routers.DefaultRouter()

router.register(r'', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', LoginView.as_view(), name='login'),

]

urlpatterns += router.urls
