from django import forms

from .models import Stores

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border-gray-300 focus:border-teal-500 focus:ring-teal-500'

class NewStore(forms.ModelForm):
    class Meta:
        model = Stores
        fields = {'category', 'name', 'description', 'price', 'image', 'image1', 'image2', 'contact', 'address'}
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES + ' bg-white',
                'placeholder': 'Select Category'
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Store Name'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES + ' h-32',
                'placeholder': 'Store Description'
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Item Price'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'image1': forms.ClearableFileInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'image2': forms.ClearableFileInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'contact': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Contact'
            }),
            'address': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Store address'
            }),
        }


class EditStore(forms.ModelForm):
        class Meta:
            model = Stores
            fields = {'name', 'description', 'price', 'image', 'is_sold', 'image1', 'image2', 'contact', 'address'}
            widgets = {               
                'name': forms.TextInput(attrs={
                    'class': INPUT_CLASSES
                }),
                'description': forms.Textarea(attrs={
                    'class': INPUT_CLASSES
                }),
                'price': forms.TextInput(attrs={
                    'class': INPUT_CLASSES
                }),
                'image': forms.ClearableFileInput(attrs={
                    'class': INPUT_CLASSES
                }),
                'image1': forms.ClearableFileInput(attrs={
                'class': INPUT_CLASSES,
                }),
                'image2': forms.ClearableFileInput(attrs={
                    'class': INPUT_CLASSES,
                }),
                'contact': forms.TextInput(attrs={
                    'class': INPUT_CLASSES,                    
                }),
                'address': forms.TextInput(attrs={
                    'class': INPUT_CLASSES,
                   
                }),
            }
        
