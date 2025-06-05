from django.contrib import admin
from homepage.models import Artikel

@admin.register(Artikel)
class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'content', 'image', 'image_description')