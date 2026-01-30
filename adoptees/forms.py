from django import forms
from .models import Adoptee        
        
class Adoptee_Show_Form(forms.ModelForm):
    class Meta:
        model = Adoptee
        exclude = ["agency","record_created_at", "record_updated_at", "record_active"]
        # fields = '__all__' # ['name','address','phone_number'] # Specify which fields to include in the form

class Adoptee_Create_Form(forms.ModelForm):
    class Meta:
        model = Adoptee
        exclude = ["created_at", "updated_at", "agency", "adopted_pet_name"]
        # fields = '__all__' # ['name','address','phone_number'] # Specify which fields to include in the form
        # Alternatively, you can use `exclude = ['created_at']` to exclude specific fields

class Adoptee_Update_Form(forms.ModelForm):
    class Meta:
        model = Adoptee
        exclude = ["record_created_at", "record_updated_at"]
        # fields = ['name','animal_type','avatar','description'] # Specify which fields to include in the form
        # Alternatively, you can use `exclude = ['created_at']` to exclude specific fields

class Adoptee_Delete_Form(forms.ModelForm):
    class Meta:
        model = Adoptee
        exclude = ["record_created_at", "record_updated_at"]
        # fields = ['name','animal_type','avatar','description'] # Specify which fields to include in the form

class Adoptee_List_Form(forms.ModelForm):
    class Meta:
        model = Adoptee
        exclude = ["record_created_at", "record_updated_at"]
        # fields = ['name','animal_type','avatar','description'] # Specify which fields to include in the form        
        