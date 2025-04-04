from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.db import transaction
import time
from .models import Persona
from .forms import PersonaForm


@never_cache
def student_list(request):
    students = Persona.objects.filter(rol='student').order_by('-id')
    return render(request, 'centre/student_list.html', {
        'students': students,
        'last_update': time.time()
    })


@never_cache
def teacher_list(request):
    teachers = Persona.objects.filter(rol='teacher').order_by('-id')
    return render(request, 'centre/teacher_list.html', {
        'teachers': teachers,
        'last_update': time.time()
    })


@transaction.atomic
def persona_create(request, rol):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.rol = rol
            persona.save()
            messages.success(request, f"{'Professor' if rol == 'teacher' else 'Alumne'} afegit correctament!")
            return redirect('centre:{}_list'.format(rol))
        else:
            messages.error(request, "Si us plau, corregeix els errors sota")
    else:
        form = PersonaForm(initial={'rol': rol})

    return render(request, 'centre/persona_form.html', {
        'form': form,
        'title': 'Afegir {}'.format('Professor/a' if rol == 'teacher' else 'Alumne/a')
    })


def persona_update(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            messages.success(request, "Registre actualitzat correctament!")
            return redirect('centre:{}_list'.format(persona.rol))
    else:
        form = PersonaForm(instance=persona)

    return render(request, 'centre/persona_form.html', {
        'form': form,
        'title': 'Editar {}'.format(persona.get_rol_display())
    })


def persona_delete(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    rol = persona.rol
    if request.method == 'POST':
        persona.delete()
        messages.success(request, "Registre eliminat correctament!")
        return redirect('centre:{}_list'.format(rol))

    return render(request, 'centre/persona_confirm_delete.html', {'persona': persona})