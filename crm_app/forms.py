#creating form for register, login and logout.
#usually creating the forms with custom fiels but there is an in-built creation form in auth.forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Record
from django.forms.widgets import PasswordInput,TextInput
from django.contrib.auth.models import User
class createUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())

class CreateRecordForm(forms.ModelForm):
    # record=Record()

    class Meta:
        model=Record
        fields=['first_name','last_name','email','phone','city','province','country']


class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model=Record
        fields=['first_name','last_name','email','phone','city','province','country']

