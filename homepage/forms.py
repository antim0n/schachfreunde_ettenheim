from django import forms
from django.forms import ModelForm
from .models import Artikel
from .models import Termin

class ArtikelForm(ModelForm):
    class Meta():
        model = Artikel
        fields = '__all__'

        labels = {
            'title': '',
            'date':  '',
            'content':  '',
            'image': '',
            'image_description': '',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Titel'}),
            'date':  forms.DateInput(attrs={'class':'form-control', "type": "date"}),
            'content':  forms.Textarea(attrs={'class':'form-control', 'placeholder':'Inhalt'}),
            'image':  forms.FileInput(attrs={'class':'form-control'}),
            'image_description':  forms.Textarea(attrs={'class':'form-control', 'placeholder':'Bildbeschreibung'}),
        }

class TerminForm(ModelForm):
    class Meta():
        model = Termin
        fields = '__all__'

        labels = {
            'title': '',
            'date': '',
            'starttime': '',
            'endtime': '',
            'location': '',
            'note': '',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Titel'}),
            'date': forms.DateInput(attrs={'class':'form-control', "type": "date"}),
            'starttime': forms.TimeInput(attrs={'class':'form-control', "type": "time"}),
            'endtime': forms.TimeInput(attrs={'class':'form-control', "type": "time"}),
            'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ort'}),
            'note': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Hinweise'}),
        }