from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import registration, Application, status
from django.forms import ModelForm

class StudentRegistration(UserCreationForm):
    class Meta:
        model = registration
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 
                    'first_name', 'idNumber', 'major']
        # or fields = __all__'

class ReceiverRegistration(UserCreationForm):
    class Meta:
        model = registration
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 
                    'first_name', 'idNumber', 'userType']

class thesisApplication(ModelForm):
    class Meta:
        model = Application
        fields = ['proponents','thesisTitle']

class applicationStatus(ModelForm):
    class Meta:
        model = status
        fields = ['dit','oaa','ocl','ore','adviser','fic']

