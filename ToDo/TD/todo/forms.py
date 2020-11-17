from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(max_length=40, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your tasks e.g. "Go to the gym at 5 PM"',
               'aria-label': 'Todo', 'aria-describedby': 'add-btn'}
    ))


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

