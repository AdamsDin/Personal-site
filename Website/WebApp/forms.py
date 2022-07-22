from .models import Task
from django.forms import ModelForm, widgets, TextInput


class Taskform(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description"]
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact type'}),
                   "description": TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter data'})}