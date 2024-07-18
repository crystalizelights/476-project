from django import forms

from .models import Stores

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border-gray-300 focus:border-teal-500 focus:ring-teal-500'

class NewStore(forms.ModelForm):
    class Meta:
        model = Stores
        fields = ['category', 'name', 'description', 'price', 'image', 'item1name', 'image1','item2name', 'image2','item3name', 'contact', 'address']
        labels = {
            'category' : 'Section',
            'image': 'First item image',
            'image1': 'Second item image',
            'image2': 'Third item image',
            'item1name': 'First item name',
            'item2name': 'Second item name',
            'item3name': 'Third item name',
        }
        widgets = {
            'category': forms.Select(attrs={
                'class': 'text-input' + ' bg-white',
                'placeholder': 'Select Category'
            }),
            'name': forms.TextInput(attrs={
                'class': 'text-input',
                'placeholder': 'Store Name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'text-input' + ' h-32 pt-3',
                'placeholder': 'Store Description'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'text-input',
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
                'class': 'text-input',
                'placeholder': 'Contact'
            }),
            'address': forms.TextInput(attrs={
                'class': 'text-input',
                'placeholder': 'Store address'
            }),
            'item1name': forms.TextInput(attrs={
                'class': 'text-input',
                'placeholder': 'Item 1 Name'
            }),
            'item2name': forms.TextInput(attrs={
                'class': 'text-input',
                'placeholder': 'Item 2 Name'
            }),
            'item3name': forms.TextInput(attrs={
                'class': 'text-input',
                'placeholder': 'Item 3 Name'
            }),
        }


class EditStore(forms.ModelForm):
        class Meta:
            model = Stores
            fields = ['category', 'name', 'description', 'price', 'image', 'item1name', 'image1','item2name', 'image2','item3name', 'contact', 'address']
            labels = {
            'category' : 'Section',
            'image': 'First item image',
            'image1': 'Second item image',
            'image2': 'Third item image',
            'item1name': 'First item name',
            'item2name': 'Second item name',
            'item3name': 'Third item name',
        }
            widgets = {               
                'name': forms.TextInput(attrs={
                    'class': 'text-input'
                }),
                'description': forms.Textarea(attrs={
                    'class':'text-input'+ ' h-32 pt-3'
                }),
                'price': forms.TextInput(attrs={
                    'class': 'text-input'
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
                    'class': 'text-input',                    
                }),
                'address': forms.TextInput(attrs={
                    'class': 'text-input',                  
                }),
                'item1name': forms.TextInput(attrs={
                'class': 'text-input',                
                }),
                'item2name': forms.TextInput(attrs={
                    'class': 'text-input',                    
                }),
                'item3name': forms.TextInput(attrs={
                    'class': 'text-input',                   
                }),
            }
        
