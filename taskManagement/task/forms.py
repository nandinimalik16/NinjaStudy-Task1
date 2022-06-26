from django import forms
from django.core.validators import MinLengthValidator

class studentRegistrationForm(forms.Form):
    name= forms.CharField(max_length=50)
    email = forms.EmailField(max_length=60)
    password=forms.CharField(max_length=50)
    phone = forms.CharField(max_length=10,validators=[MinLengthValidator(10)])
    gender=forms.ChoiceField(choices=(("Male","Male"),("Female","Female"),("Other","Other")))
    country=forms.CharField(max_length=50)
    # experience=forms.CharField(max_length=50)

class teacherRegistrationForm(forms.Form):
    name= forms.CharField(max_length=50)
    email = forms.EmailField(max_length=60)
    password=forms.CharField(max_length=50)
    phone = forms.CharField(max_length=10,validators=[MinLengthValidator(10)])
    gender=forms.ChoiceField(choices=(("Male","Male"),("Female","Female"),("Other","Other")))
    country=forms.CharField(max_length=50)
    experience=forms.CharField(max_length=50)
