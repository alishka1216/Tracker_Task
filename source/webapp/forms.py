from django import forms
from django.core.validators import MinValueValidator
from webapp.models import Status, Type


class TrackerForm(forms.Form):

    title = forms.CharField(max_length=120, required=True)
    description = forms.CharField(max_length=3000, required=True, widget=forms.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True,  initial='new')
    type = forms.ModelMultipleChoiceField(required=False, label='Типы', queryset=Type.objects.all())
