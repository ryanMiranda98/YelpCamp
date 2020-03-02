from django.urls import path
from . import views

urlpatterns = [
    path('', views.showAllCamps, name='all_camps'),
    path('new/', views.createCamp, name='create_camp'),
    path('<int:pk>/', views.showCamp, name='camp'),
    path('update/<int:pk>', views.updateCamp, name='update_camp'),
]