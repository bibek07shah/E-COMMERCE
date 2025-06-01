# forms.py
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'dob']
        widgets = {
            'profile_picture': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'bio': forms.Textarea(attrs={'class': 'custom-textarea', 'rows': 5, 'placeholder': 'Tell us about yourself...'}),
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'custom-date-input'}),
        }