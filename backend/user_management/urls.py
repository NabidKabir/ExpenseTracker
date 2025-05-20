from django.urls import path
from . import views

urlpatterns = [
    path('user_management/', views.user_management, name='user_management')
]

