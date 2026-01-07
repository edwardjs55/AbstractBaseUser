from django import forms
from .models import Agency        


class Agency_New_Form(forms.ModelForm):
    class Meta:
        model = Agency
        exclude = ["created_at", "updated_at", "director", "staff"]
        # fields = '__all__' # ['name','address','phone_number'] # Specify which fields to include in the form
        # Alternatively, you can use `exclude = ['created_at']` to exclude specific fields

class Agency_Update_Form(forms.ModelForm):
    class Meta:
        model = Agency
        exclude = ["created_at", "updated_at", "director"]
        #fields = ['name','animal_type','avatar','description'] # Specify which fields to include in the form
        # Alternatively, you can use `exclude = ['created_at']` to exclude specific fields