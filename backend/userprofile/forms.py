from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['biography', 'cv', 'profile_picture']
        widgets = {
            'biography': forms.Textarea(attrs={'class': 'form-control'}),
            'cv': forms.FileInput(attrs={'class': 'form-control-file'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control-file'}),
        }