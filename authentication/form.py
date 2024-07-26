from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreation(UserCreationForm):
    password1 = forms.CharField(
        label="password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"})

    )

    password2 = forms.CharField(
        label="confirm password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"})

    )

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("password1", "password2")
