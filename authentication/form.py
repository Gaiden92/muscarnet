from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):

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


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, label="Entrez nom d'utilisateur")
    password = forms.CharField(max_length=65, widget=forms.PasswordInput, label="Entrez votre mot de passe")