from django.contrib import admin
from homepage.models import Artikel
from homepage.models import Termin

@admin.register(Artikel)
class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'content', 'image', 'image_description')

@admin.register(Termin)
class TerminAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'starttime', 'endtime', 'location', 'note')