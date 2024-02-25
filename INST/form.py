from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User


class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["id"] = "username"
        self.fields["username"].widget.attrs["class"] = "psw"
        self.fields["username"].widget.attrs["placeholder"] = "Write username"

        self.fields["password1"].widget.attrs["id"] = "password1"
        self.fields["password1"].widget.attrs["class"] = "psw"
        self.fields["password1"].widget.attrs["placeholder"] = "Write password"

        self.fields["password2"].widget.attrs["id"] = "password2"
        self.fields["password2"].widget.attrs["class"] = "psw"
        self.fields["password2"].widget.attrs["placeholder"] = "Repeat password"

        self.fields["email"].widget.attrs["id"] = "email"
        self.fields["email"].widget.attrs["class"] = "psw"
        self.fields["email"].widget.attrs["placeholder"] = "Write email"


class LogIn(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["id"] = "username"
        self.fields["username"].widget.attrs["class"] = "psw"
        self.fields["username"].widget.attrs["placeholder"] = "Write username"
        self.fields["password"].widget.attrs["id"] = "password"
        self.fields["password"].widget.attrs["class"] = "psw"
        self.fields["password"].widget.attrs["placeholder"] = "Write password"


class ProfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "status", "my_web"]
        widgets = {"username": forms.TextInput(attrs={"id": "name", "class": "psw", "placeholder": "Write username"}),
                   "status": forms.TextInput(attrs={"id": "status", "class": "psw", "placeholder": "Write status"}),
                   "my_web": forms.TextInput(attrs={"id": "my_web", "class": "psw", "placeholder": "Write web"})}


class Security(forms.ModelForm):
    class Meta:
        model = User
        fields = ["password", "password"]
        widgets = {"password": forms.PasswordInput(attrs={"id": "password1", "class": "psw", "placeholder": "Repeat password"}),
                   "password": forms.PasswordInput(attrs={"id": "password2", "class": "psw", "placeholder": "Repeat password"})}


class ModForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email"]
        widgets = {"email": forms.EmailInput(attrs={"id": "email", "class": "psw", "placeholder": "Wtite email"})}


class PersonalForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]
        widgets = {"last_name": forms.TextInput(attrs={"id": "last_name", "class": "psw", "placeholder": "Write last name"}),
                   "first_name": forms.TextInput(attrs={"id": "first_name", "class": "psw", "placeholder": "Write first name"})}