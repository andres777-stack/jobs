from django import forms
from jobs.models import *

class JobForm(forms.ModelForm):
    #validaciones:

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 4:
            self.add_error('title', 'title debe tener al menos cuatro caracteres')
        return title
    
    def clean_desc(self):
        desc = self.cleaned_data['desc']
        if len(desc) < 10:
            self.add_error('desc', 'La descripción debe tener más de 10 caracteres')
        return desc

    #Campos añadidos al formulario

    #meta, fields, label, widget

    class Meta:
        model = Job
        
        fields = ['title', 'desc', 'location' ]
        
        labels = {
            'title' : 'Title: ',
            'desc' : 'Descripción: ',
            'location' : 'Location'
        }
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'desc' : forms.Textarea(attrs={'class': 'form-control'}),
            'location' : forms.TextInput(attrs={'class': 'form-control'}),
        }
