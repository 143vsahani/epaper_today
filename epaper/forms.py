from django import forms
from .models import Epaper

class EpaperForm(forms.ModelForm):
    class Meta:
        model = Epaper
        fields = ['title', 'file', 'description', 'is_published']
