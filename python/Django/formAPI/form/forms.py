from dataclasses import fields
from django import forms
from form.models import Student

class LoginForm(forms.Form):
    user_name = forms.CharField(label="Enter User Name" ,max_length=35, required=False)
    password = forms.CharField(max_length=20, help_text="Password cannot be more than 20 characters", widget=forms.PasswordInput)
    age = forms.IntegerField()
    keep_signed_in = forms.BooleanField()
    address = forms.CharField(max_length=300, widget=forms.Textarea(
        attrs={'class' : 'form-input', 'title' : 'Enter the address here'}
        ))


BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class SimpleForm(forms.Form):
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=FAVORITE_COLORS_CHOICES,
    )

class StudentForm(forms.ModelForm):
    # genders = [
    #    ('male', 'Male'),
    #     ('female', 'Female'),
    # ]
    # gender = forms.MultipleChoiceField(widget=forms.RadioSelect, choices=genders)
    class Meta:
        model = Student
        # fields = ('name', 'std', 'address')
        fields = '__all__'