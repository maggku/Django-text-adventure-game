from django import forms

class RegisterForm(forms.Form):
  name = forms.CharField(max_length=64)
  email = forms.EmailField()
  country = forms.CharField(max_length=64)
  age = forms.IntegerField()
