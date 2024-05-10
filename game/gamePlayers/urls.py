from django.urls import path
from . import views
urlpatterns = [
    path('gamePlayers/', views.playerName, name="PlayersName"),
    path('gamePlayers/informations', views.informations, name="PlayerInfos"),
]