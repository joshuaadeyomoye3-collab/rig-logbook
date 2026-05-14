from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_list, name='log_list'),
    path('log/<int:pk>/', views.log_detail, name='log_detail'),
    path('logs/incidents/', views.log_filtered, name='log_filtered'),
]