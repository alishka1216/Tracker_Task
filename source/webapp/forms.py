from django import forms
from django.core.validators import MinValueValidator, ValidationError
from webapp.models import Status, Type, Tracker, Project


class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ['title', 'description', 'status', 'type']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'date']
        
        
class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти' )