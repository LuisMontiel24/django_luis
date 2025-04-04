from django.core.management.base import BaseCommand
from centre.models import Persona
from datetime import date


class Command(BaseCommand):
    help = 'Popula la base de datos con datos iniciales'

    def handle(self, *args, **options):
        # Datos de ejemplo para alumnos
        students = [
            {'nom': 'Anna', 'cognom1': 'Garcia', 'cognom2': 'Martínez',
             'correu': 'anna.garcia@itic.cat', 'curs': 'DAW2A',
             'moduls': 'M06, M07, M08, M09', 'rol': 'student'},

            {'nom': 'Pau', 'cognom1': 'Rodríguez', 'cognom2': 'López',
             'correu': 'pau.rodriguez@itic.cat', 'curs': 'DAW2A',
             'moduls': 'M06, M07, M08, M09', 'rol': 'student'},

            {'nom': 'Laia', 'cognom1': 'Fernández', 'cognom2': 'Sánchez',
             'correu': 'laia.fernandez@itic.cat', 'curs': 'DAW2A',
             'moduls': 'M06, M07, M08, M09', 'rol': 'student'}
        ]

        # Datos de ejemplo para profesores
        teachers = [
            {'nom': 'Roger', 'cognom1': 'Sobrino', 'cognom2': 'Gil',
             'correu': 'roger.sobrino@itic.cat', 'curs': 'DAM2B, DAW2A',
             'moduls': 'M06, M07', 'rol': 'teacher', 'tutor': True},

            {'nom': 'Josep', 'cognom1': 'Oriol', 'cognom2': 'Roca',
             'correu': 'josep.oriol@itic.cat', 'curs': 'DAW2B, DAW2A, DAW1A',
             'moduls': 'M03, M07', 'rol': 'teacher', 'tutor': False},

            {'nom': 'Juanma', 'cognom1': 'Biel', 'cognom2': 'Pérez',
             'correu': 'juanma.biel@itic.cat', 'curs': 'DAW2B, DAW2A',
             'moduls': 'M04, M05', 'rol': 'teacher', 'tutor': True}
        ]

        for data in students + teachers:
            Persona.objects.get_or_create(**data)

        self.stdout.write(self.style.SUCCESS('Base de datos poblada correctamente con datos de ejemplo'))