from django import forms
from django.core.exceptions import ValidationError

from .models import ToDo

class MyToDoForm(forms.ModelForm):
    tache = forms.CharField(max_length=1000, label='', widget=forms.TextInput(attrs={
        'placeholder': 'Entrer votre Tache'
    }))
    class Meta:
        model = ToDo
        fields = ('tache', )
    
    # def clean_nom(self):
    #     tache = self.cleaned_data["tache"]
    #     if 'abs' not in tache:
    #        raise ValidationError("La tache doit contenir abs!")
    #     return tache

