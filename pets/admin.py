from django.contrib import admin
from .models import MyPets

# Register your models here.
class CustomUserModelAdmin(admin.ModelAdmin):
        list_display = ('name', 'animal_type','user') # Fields to display in the list view
        search_fields = ('user', 'name','animal_type') # Fields to search by
        fields = ('user',('name','animal_type','description'),
                  'bday','avatar','color','weight','source','diet','notes',
                  'veterinary','litter_family','location',
                  ('health_rating','health_status','health_issues'),
                  'expired'
                )    

        # ... other customizations
        
        readonly_fields = ('created_at','last_modified')

admin.site.register(MyPets,CustomUserModelAdmin)