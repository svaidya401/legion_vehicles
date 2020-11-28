from django.urls import path, include
from bikes_app import views

app_name = 'bikes_app'
urlpatterns = [
    path('', views.bikesHome, name='bikesHome'),
    path('<int:id>', views.bikeDetails, name='bikeDetails')
]
