from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aktuelles/', views.aktuelles, name='aktuelles'),
    path('der_verein/', views.der_verein, name='der_verein'),
    path('termine/', views.termine, name='termine'),
    path('sponsorenbrett/', views.sponsorenbrett, name='sponsorenbrett'),
    path('kleidung/', views.kleidung, name='kleidung'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('impressum/', views.impressum, name='impressum'),
]