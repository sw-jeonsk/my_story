from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

from .models import Writer


class WriterCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = Writer
        fields = ("email", "name")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# 사용자의 자기 정보 변경 폼
class CustomWriterChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = ("email", "password", "name", "is_superuser", "is_staff", "created_at")

    def clean_password(self):
        return self.initial["password"]

    def save(self, commit=True):
        user = super().save(commit=False)
        if not user.is_superuser and user.is_staff:
            raise forms.ValidationError("if is_staff True, is_superuser must True")
        return user
