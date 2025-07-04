from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nickname = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'nickname')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data.get('nickname', '')
        
        if commit:
            user.save()

        return user 