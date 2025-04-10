from django.forms import ModelForm
from .models import *
from django import forms

class chatMessageCreateForm(ModelForm):
  class Meta:
    model = GroupMessages
    fields = ['body']
    widgets = {
      'body': forms.TextInput(attrs={'placeholder': 'Add message...', 'class': 'p-4'})
    }