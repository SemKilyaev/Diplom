from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'
    

class TodoForm(forms.Form):
    make_up = forms.DateField(initial=datetime.date.today(), widget=DateInput(
        attrs={'class': 'form-control', 'aria-label': 'Todo'}
    ))
    text = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your tasks e.g. "Go to the gym at 5 PM"',
               'aria-label': 'Todo', 'aria-describedby': 'add-btn'}
    ))
    
class ExampleTodoForm(forms.Form):
    class Meta:
        widgets = {'make_up': DateInput()}   

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']









