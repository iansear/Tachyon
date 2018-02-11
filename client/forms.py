from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms import CharField
from django.forms import BooleanField
from django.forms import DurationField
from django.forms import IntegerField
from django.forms import DecimalField
from django.forms import EmailField
from django.forms import PasswordInput
from delivery.models import Client
from delivery.models import Job

class RegisterClientForm(ModelForm):

    alias = CharField(label = ("Alias"))
    phone = CharField(label = ("Your Phone"))
    
    class Meta:
        model = Client
        fields = ['alias', 'phone']

class RegisterUserForm(UserCreationForm):

    error_messages = { 'password_mismatch': ("The two passwords do not match."),}
    
    password1 = CharField(label = ("Password"),
                widget = PasswordInput)
    
    password2 = CharField(label = ("Password Confirmations"),
                widget = PasswordInput,
                help_text = ("Enter the same password as above."))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
