from django.urls import path
from . import views

urlpatterns = [
    path('app1/', views.users, name='app1')
]