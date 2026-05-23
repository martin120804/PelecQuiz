from django import forms
from .models import EventRegistration

class EventRegistrationForm(forms.ModelForm):

    class Meta:
        model = EventRegistration
        fields = ['full_name', 'email', 'age', 'password']

        widgets = {
            'password': forms.PasswordInput(),
        }

    # Full Name Validation
    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')

        if len(full_name) < 5:
            raise forms.ValidationError(
                "Full name must be at least 5 characters."
            )

        return full_name

    # Email Validation
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email.endswith('@gmail.com'):
            raise forms.ValidationError(
                "Email must end with @gmail.com"
            )

        return email

    # Age Validation
    def clean_age(self):
        age = self.cleaned_data.get('age')

        if age < 18:
            raise forms.ValidationError(
                "Age must be 18 or above."
            )

        return age

    # Password Validation
    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 8:
            raise forms.ValidationError(
                "Password must be at least 8 characters."
            )

        return password