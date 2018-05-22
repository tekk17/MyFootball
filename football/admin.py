from django.contrib import admin

# Register your models here.
from .models import footballClub, footballPlayers
#from football.models import playingPosition

admin.site.register(footballClub)
admin.site.register(footballPlayers)
#admin.site.register(playingPosition)