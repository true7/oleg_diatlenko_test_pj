from django import forms
from django.forms import ModelForm
from .models import Note

class NoteForm(ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'class': "form-control", 'placeholder': 'Title...'}
            )
        )
    content = forms.CharField(
        label='',
        min_length=10,
        widget=forms.Textarea(
            attrs={'class': "form-control", 'placeholder': 'Content...'}
            )
        )

    class Meta:
        model = Note
        fields = ['title', 'content','image']
