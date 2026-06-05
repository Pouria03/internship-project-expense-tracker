from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': 'دو رمز عبور وارد شده با هم مطابقت ندارند.',
    }

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'نام کاربری'
        self.fields['username'].help_text = 'حداکثر ۱۵۰ کاراکتر. حروف، اعداد و @/./+/-/_ مجاز است.'
        self.fields['username'].error_messages = {
            'required': 'نام کاربری الزامی است.',
            'unique': 'این نام کاربری قبلاً ثبت شده است.',
            'invalid': 'نام کاربری معتبر نیست.',
        }
        self.fields['password1'].label = 'رمز عبور'
        self.fields['password1'].help_text = None
        self.fields['password1'].error_messages = {
            'required': 'رمز عبور الزامی است.',
        }
        self.fields['password2'].label = 'تأیید رمز عبور'
        self.fields['password2'].help_text = None
        self.fields['password2'].error_messages = {
            'required': 'تأیید رمز عبور الزامی است.',
        }

        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'نام کاربری یا رمز عبور اشتباه است.',
        'inactive': 'این حساب کاربری غیرفعال است.',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'نام کاربری'
        self.fields['password'].label = 'رمز عبور'

        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})