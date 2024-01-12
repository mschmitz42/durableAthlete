from django.urls import path
from durabilityBuilder import views


app_name = 'durabilityBuilder'


urlpatterns = [
    path('', views.durabilityBuilder_index, name='durabilityBuilder-index'),
    path('home', views.durabilityBuilder_index, name='home'),
    path('send_confirm', views.send_confirmation, name='send_confirm'),
    path('get_started', views.get_started, name='get_started'),
]
