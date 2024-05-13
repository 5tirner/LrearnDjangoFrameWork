from django.urls import path
from . import views

urlpatterns = [
    path('statistic/', views.names, name="Users Name"),
    path('', views.start, name="Lunch"),
]