from django.db import models

class Persona(models.Model):
    ROLES = (
        ('teacher', 'Professor/a'),
        ('student', 'Alumne/a'),
    )

    nom = models.CharField(max_length=50, verbose_name="Nom")
    cognom1 = models.CharField(max_length=50, verbose_name="Primer Cognom")
    cognom2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Segon Cognom")
    correu = models.EmailField(verbose_name="Correu electrònic")
    curs = models.CharField(max_length=100, verbose_name="Curs")
    moduls = models.TextField(verbose_name="Mòduls")
    rol = models.CharField(max_length=7, choices=ROLES, verbose_name="Rol")
    tutor = models.BooleanField(default=False, verbose_name="Tutor")

    def __str__(self):
        return f"{self.nom} {self.cognom1}"

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Persones"