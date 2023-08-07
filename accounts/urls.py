
from django.urls import path, include
from accounts import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('register/', views.Register, name="user-register"),
    path('login/', views.Login, name="user-login"),
    path('logout/', views.LogoutUser, name="logout-user"),
    
    path('change-password/', views.change_password, name="change_password"),
    
    path('forgot-password/', views.ForgotPassword, name="forgot-password"),


]
