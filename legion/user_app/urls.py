from django.urls import path, include
from user_app import views

app_name = 'user_app'
urlpatterns = [
    path('info', views.user_info, name='info'),
    path('login', views.user_login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.user_logout, name='logout'),
]
