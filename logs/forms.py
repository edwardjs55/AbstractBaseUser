from django import forms
from .models import LogEntry

class MyPetsLogForm(forms.ModelForm):
    class Meta:
        model = LogEntry
        fields = ['category','action'] # Specify which fields to include in the form
        # Alternatively, you can use `exclude = ['created_at']` to exclude specific fields