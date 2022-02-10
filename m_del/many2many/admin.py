from django.contrib import admin
from .models import Singer, Song

# Register your models here.
@admin.register(Singer)
class singeradmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Song)
class songadmin(admin.ModelAdmin):
    list_display = ['song_name', 'duration', 'own_by']
