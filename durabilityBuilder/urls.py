from django.urls import path, include
from durabilityBuilder import views


app_name = 'durabilityBuilder'




urlpatterns = [
    path('', views.durabilityBuilder_index, name='durabilityBuilder-index'),
]
