from django.urls import path
from users import views

urlpatterns = [
    path('<int:pk>/profile', views.profile, name='profile'),
]