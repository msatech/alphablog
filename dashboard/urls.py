
from django.urls import path, include
from dashboard import views
urlpatterns = [
    
    path('dashboard/', views.Dashbaord, name="dashboard"),
]
