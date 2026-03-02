from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields=['firstname','lastname','age','course']
    widgets = {
         'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
         'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
         'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}),
         'course': forms.Select(choices=[
           ('Full Stack Development', 'Full Stack Development'),
             ('Data Science', 'Data Science'),
               ('Cybersecurity', 'Cybersecurity'),
               ('Cloud Computing', 'Cloud Computing'),
               ('Mobile App Development', 'Mobile App Development'),
               ('UI/UX Design', 'UI/UX Design'),
               ('Artificial Intelligence', 'Artificial Intelligence'),
         ]
         ,attrs={'class': 'form-control'}),
    }
class RegisterForm(UserCreationForm):
        class Meta:
            model = User
            fields = ['username','first_name','last_name','email', 'password1', 'password2']
