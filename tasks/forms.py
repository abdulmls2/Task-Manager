from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms
from .models import *


# Form for the user registration
class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("email", "username", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Username"
        self.fields["email"].label = "Email address"


# Form to create task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'importance', 'ending_date']
        widgets = {
            # custom field calendar
            'creation_date': forms.DateInput(attrs={'type': 'date'}),
            'ending_date': forms.DateInput(attrs={'type': 'date'}),
        }

# Form to edit task
class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'importance', 'ending_date', 'complete']
        widgets = {
            # custom field calendar
            'creation_date': forms.DateInput(attrs={'type': 'date'}),
            'ending_date': forms.DateInput(attrs={'type': 'date'}),
        }