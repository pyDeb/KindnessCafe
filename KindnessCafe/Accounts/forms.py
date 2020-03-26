from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, get_user_model
from django.contrib.auth.models import User
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            # 'username': forms.EmailInput(attrs={
            #     'placeholder': 'Email',
            # }),
            'username': forms.HiddenInput,
        }

    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)


    
    def save(self, commit=True):
        user = super().save(False)
        user.username = user.email
        user = super().save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']