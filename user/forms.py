form django import forms
form django.contrib.auth.models import User #importation dde user de django
from . import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm #importation des formuler des creations et modifications de profil

class RegistrationForm(UserCreationForm):
    model = User
    field = (
        'username',
        'email',
        'firstname',
        'lastname',
        'password1',
        'password2',
    ) 