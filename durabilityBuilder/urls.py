from django.urls import path, include
from durabilityBuilder import views


app_name = 'durabilityBuilder'


urlpatterns = [
    path('', views.dashboard, name='durabilitybuilder_index'),
    path('home', views.dashboard, name='home'),
    path('send_confirm', views.send_confirmation, name='send_confirm'),
    path('get_started', views.get_started, name='get_started'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('under_construction/', views.under_construction, name='under_construction'),
    path('intro_day1/', views.intro_day1, name='intro_day1'),
    path('intro_day2/', views.intro_day2, name='intro_day2'),
    path('intro_day3/', views.intro_day3, name='intro_day3'),
    path('intro_day4/', views.intro_day4, name='intro_day4'),
    path('intro_day5/', views.intro_day5, name='intro_day5'),
    path('intro_day6/', views.intro_day6, name='intro_day6'),
    path('intro_day7/', views.intro_day7, name='intro_day7'),
    path('intro_day8/', views.intro_day8, name='intro_day8'),
    path('intro_day9/', views.intro_day9, name='intro_day9'),
    path('intro_day10/', views.intro_day10, name='intro_day10'),
    path('intro_day11/', views.intro_day11, name='intro_day11'),
    path('intro_day12/', views.intro_day12, name='intro_day12'),
    path('intro_day13/', views.intro_day13, name='intro_day13'),
    path('intro_day14/', views.intro_day14, name='intro_day14'),
]
