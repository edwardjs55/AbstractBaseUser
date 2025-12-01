from django import forms
from .models import MyPets

class MyPetsForm(forms.ModelForm):
    class Meta:
        model = MyPets
        fields = ['name','animal_type','description'] # Specify which fields to include in the form
        # Alternatively, you can use `exclude = ['created_at']` to exclude specific fields