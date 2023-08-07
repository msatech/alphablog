
from django.urls import path, include
from alphacs import views
urlpatterns = [
    
    path('', views.Home, name="home"),
    path('contactus/', views.ContactUs, name="contact-us"),
    path('erp-development/', views.Erp, name="erp"),
    path('cloud-service-management/', views.Cloud, name="cloud"),
    path('crm-custom-development', views.Crm, name="crm"),
    path('website-design-development/', views.Web, name="web"),
    path('android-mobile-app-development/', views.Mobile, name="mobile"),
    path('seo-digital-marketing/', views.Seo, name="seo"),
    path('contact-form/', views.ContactForm, name="contact-form"),






]
