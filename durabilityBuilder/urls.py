from django.urls import path
from durabilityBuilder import views


app_name = 'durabilityBuilder'


urlpatterns = [
    path('', views.durabilitybuilder_index, name='durabilitybuilder_index'),
    path('home', views.durabilitybuilder_index, name='home'),
    path('send_confirm', views.send_confirmation, name='send_confirm'),
    path('get_started', views.get_started, name='get_started'),
]
