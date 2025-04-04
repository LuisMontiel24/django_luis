from django.contrib import admin
from .models import Persona

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'cognom1', 'rol', 'curs', 'tutor')
    list_filter = ('rol', 'tutor')
    search_fields = ('nom', 'cognom1', 'correu')
    fieldsets = (
        (None, {
            'fields': ('nom', 'cognom1', 'cognom2', 'correu')
        }),
        ('Informació acadèmica', {
            'fields': ('rol', 'curs', 'moduls', 'tutor')
        }),
    )