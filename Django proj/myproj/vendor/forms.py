from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import ReviewText
from .models import UserProfile

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter username',
        'class': 'text-input'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password',
        'class': 'text-input'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter username',
        'class': 'text-input'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter email address',
        'class': 'text-input'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password',
        'class': 'text-input'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password',
        'class': 'text-input'
    }))

class ReviewTextForm(forms.ModelForm):
    class Meta:
        model = ReviewText
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }

class UserSettingsForm(forms.ModelForm):
    ROLE_CHOICES = [
        ('Viewer', 'Viewer'),
        ('Seller', 'Seller'),
    ]

    userType = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'w-6 h-6',
        })
    )
    profile_image = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'class': 'uploadCustom pl-4'
    }))

    class Meta:
        model = UserProfile
        fields = ['userType', 'profile_image']
