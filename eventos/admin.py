from django.contrib import admin
from .models import Evento, Local, Participante

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'local', 'ativo')
    list_filter = ('data', 'ativo')
    search_fields = ('titulo',)

admin.site.register(Local)
admin.site.register(Participante)
