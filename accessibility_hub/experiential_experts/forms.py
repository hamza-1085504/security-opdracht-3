from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from administrators.models import Ervaringsdeskundige
from django.forms.widgets import PasswordInput, TextInput
from django.core.exceptions import ValidationError

class CreateExpertForm(forms.Form):
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class LoginFormExpert(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    wachtwoord = forms.CharField(label='wachtwoord', widget = forms.PasswordInput)