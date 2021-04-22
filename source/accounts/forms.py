from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import PasswordInput
from accounts.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.CharField(max_length=30, required=True)

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean(self):
        super(UserRegisterForm, self).clean()
        if not self.cleaned_data.get('first_name') and not self.cleaned_data.get('last_name'):
            raise ValidationError('First name or last name should be registered.')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')


class UserChangePasswordForm(forms.ModelForm):
    old_password = forms.CharField(required=True, label='Старый пароль', widget=PasswordInput)
    new_password = forms.CharField(required=True, label='Новый пароль', widget=PasswordInput)
    password_confirm = forms.CharField(required=True, label='Подтверждение пароля', widget=PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('old_password', 'new_password', 'password_confirm')

    def clean_password_confirm(self):
        new_password = self.cleaned_data.get('new_password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if new_password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        return new_password

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Пароль введён не верно')

        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data.get('new_password'))
        if commit:
            user.save()
        return user
