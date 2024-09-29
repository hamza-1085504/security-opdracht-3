from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Medewerker
from django.forms.widgets import PasswordInput, TextInput

class CreateEmployeeForm(forms.ModelForm):
    wachtwoord = forms.CharField(label='Wachtwoord', widget = forms.PasswordInput)
    
    class Meta:
        model = Medewerker
        fields = ('voornaam', 'achternaam', 'gebruikersnaam', 'wachtwoord', 'emailadres', 'postcode', 'huisnummer', 'geslacht', 'geboortedatum', 'admin')
    
    
class LoginForm(forms.Form):
    gebruikersnaam = forms.CharField(label='Gebruikersnaam', max_length=100)
    wachtwoord = forms.CharField(label='Wachtwoord', widget = forms.PasswordInput)