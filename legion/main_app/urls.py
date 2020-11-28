from django.urls import path, include
from main_app import views

app_name = 'main_app'
urlpatterns = [
    path('contact_us', views.contactUs, name='contactUs'),
]
