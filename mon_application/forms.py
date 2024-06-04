from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *




class SignUpForm(UserCreationForm):
    username = forms.CharField(label="",
                               max_length=32, help_text="<small id='emailHelp' class='form-text text-muted'>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(label="",
                                 max_length=32, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="",
                                max_length=32, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(label="",
                             max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(label="", help_text="<small><ul class='form-text text-muted'><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul></small>",
                                max_length=40, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="", help_text="<small class='form-text text-muted'>Enter the same password as before, for verification.</small>",
                                max_length=40, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
        
    
class User_cForm(forms.ModelForm):
    class Meta:
        model = User_c
        fields = ['username', 'email', 'contact', 'photo_profil', 'role']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'photo_profil': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la machine'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantité'}),
            'type_maintenance': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

class TechnicienForm(forms.ModelForm):
    class Meta:
        model = Technicien
        fields = ['username', 'first_name', 'last_name', 'email', 'contact', 'photo_profil', 'role', 'fonction', 'adresse', 'pays']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de famille'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact'}),
            'photo_profil': forms.FileInput(attrs={'class': 'form-control-file'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'fonction': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fonction'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse'}),
            'pays': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pays'}),
        }