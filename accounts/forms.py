from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])   # 해싱

        if commit:
            user.save()
        return user 
    


class ProfileForm(forms.ModelForm):
    use_default_image = forms.BooleanField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = Profile
        fields = ['nickname', 'upload_img', 'birth_date']