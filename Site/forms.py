from django import forms
from Users.models import Person

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['cover_photo','profile_photo']