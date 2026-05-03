from django import forms
from captcha.fields import CaptchaField
from .models import UserProfile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address']

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)