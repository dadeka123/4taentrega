from django.contrib import admin
from .models import Jugador, Equipo, Representante, Avatar

# Register your models here.

admin.site.register(Jugador)
admin.site.register(Equipo)
admin.site.register(Representante)
admin.site.register(Avatar)