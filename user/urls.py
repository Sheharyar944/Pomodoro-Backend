from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers
from .views import LoginView, UserRegistrationAPIView ,UserViewSet


router = routers.DefaultRouter()

router.register(r'', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('user/', UserViewSet.as_view(), name='user'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('register/register/', UserRegistrationAPIView.as_view(), name='register'),

]

urlpatterns += router.urls
