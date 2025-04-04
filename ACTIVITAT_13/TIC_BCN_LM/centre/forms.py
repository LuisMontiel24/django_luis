from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'cognom1': forms.TextInput(attrs={'class': 'form-control'}),
            'cognom2': forms.TextInput(attrs={'class': 'form-control'}),
            'correu': forms.EmailInput(attrs={'class': 'form-control'}),
            'curs': forms.TextInput(attrs={'class': 'form-control'}),
            'moduls': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
            'tutor': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'nom': 'Nom',
            'cognom1': 'Primer Cognom',
            'cognom2': 'Segon Cognom',
            'correu': 'Correu Electrònic',
            'curs': 'Curs',
            'moduls': 'Mòduls',
            'rol': 'Rol',
            'tutor': 'És tutor?',
        }