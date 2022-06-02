from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(label="Enter User Name" ,max_length=35, required=False)
    password = forms.CharField(max_length=20, help_text="Password cannot be more than 20 characters", widget=forms.PasswordInput)
    age = forms.IntegerField()
    keep_signed_in = forms.BooleanField()