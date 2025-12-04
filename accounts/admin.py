from django.contrib import admin
from .models import CustomUser,Profile

# Register your models here.
class CustomUserModelAdmin(admin.ModelAdmin):
        list_display = ('username', 'email', 'id') # Fields to display in the list view
        search_fields = ('username', 'email') # Fields to search by
        fields = ('email','username', ('first_name','last_name'),
        ('password'),('is_superuser','is_staff','is_active'),('created_at','last_login'),
        ('groups','user_permissions'))

        # ... other customizations
        
        readonly_fields = ('created_at','last_login')

admin.site.register(CustomUser,CustomUserModelAdmin)
admin.site.register(Profile)

