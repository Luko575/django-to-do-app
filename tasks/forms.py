from django import forms
from django.forms import ModelForm
from tasks.models import Task

class TaskForm(ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title ( max. 255 characters )', 'maxlength': 255}))

    class Meta:
        model = Task
        fields = ('title',)