from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="First Page"),
    path('Dashboard/', views.name, name="Users Names"),
    path('Dashboard/info/<int:id>', views.info, name="User Information")
]