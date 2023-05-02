from django import forms
from django.contrib.auth.forms import UserCreationForm

from user_app.models import CustomUser


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=320)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=320, required=True, help_text="Required")
    first_name = forms.CharField(max_length=60, required=False)
    last_name = forms.CharField(max_length=60, required=False)

    class Meta:
        model = CustomUser
        fields = ["email", "password1", "password2"]

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not first_name:
            return None

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if not last_name:
            return None
