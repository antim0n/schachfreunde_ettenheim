from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aktuelles/', views.aktuelles, name='aktuelles'),
    path('spielabend/', views.spielabend, name='spielabend'),
    path('training/', views.training, name='training'),
    path('mannschaften/', views.mannschaften, name='mannschaften'),
    path('sponsorenbrett/', views.sponsorenbrett, name='sponsorenbrett'),
    path('kleidung/', views.kleidung, name='kleidung'),
    path('impressum/', views.impressum, name='impressum'),
]