from django.urls import path
from . import views

urlpatterns = [
    path('userInformations/', views.userDetails, name='UserInfos')
]