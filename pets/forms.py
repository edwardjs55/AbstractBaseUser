from django import forms
from .models import MyPets


class MyPets_New_Form(forms.ModelForm):
    class Meta:
        model = MyPets
        fields = ['name', 'animal_type', 'avatar', 'description']
        # Alternatively, you can use `exclude = ['created_at']` to exclude specific fields

class MyPetsForm(forms.ModelForm):
    class Meta:
        model = MyPets
        exclude = ["created_at", "last_modified", "user"]
        #fields = ['name','animal_type','avatar','description'] # Specify which fields to include in the form
        # Alternatively, you can use `exclude = ['created_at']` to exclude specific fields