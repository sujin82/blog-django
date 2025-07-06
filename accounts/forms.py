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
        
        if commit:
            user.save()
        return user 
    


class ProfileForm(forms.ModelForm): # 확인
    class Meta:
        model = Profile
        fields = ['nickname', 'gender', 'profile_image', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }