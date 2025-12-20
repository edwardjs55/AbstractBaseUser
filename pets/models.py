# myapp/models.py
from django.db import models
# from accounts import CustomUser
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class MyPets(models.Model):
    
    class SexChoices(models.TextChoices):
        FEMALE = 'F', 'Female'
        MALE = 'M', 'Male'
        UNSPECIFIED = 'U', 'Unspecified'
        # You can add more comprehensive options as needed
    
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user',verbose_name='pet owner'
        )
    name = models.CharField(max_length=100,verbose_name='pet name')
    animal_type = models.CharField(max_length=100,verbose_name='animal type')
    # sex = models.CharField(max_length=100, blank=True, verbose_name='sex')
    sex = models.CharField(max_length=1, blank=True, verbose_name='sex', default=SexChoices.UNSPECIFIED, choices=SexChoices.choices)
    description = models.TextField( verbose_name='pet description',blank=True)
    bday = models.DateField(null=True, blank=True, verbose_name='birth date')
    avatar = models.ImageField(default='pet_avatars/default.jpg',upload_to='pet_avatars/',blank=True,verbose_name='pet image')    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='date created')
    last_modified = models.DateTimeField(auto_now_add=True, verbose_name='last modified')    
    color = models.CharField(max_length=100, blank=True, verbose_name='color')
    weight = models.FloatField(null=True, blank=True, verbose_name='weight (#lb)')
    source = models.CharField(max_length=255, blank=True, verbose_name='source (shelter, breeder, family tc.)')
    diet = models.CharField(max_length=255, blank=True, verbose_name='dietary preferences')
    notes = models.TextField(blank=True, verbose_name='additional notes')  
    veterinary = models.CharField(max_length=255, blank=True, verbose_name='veterinary info')
    litter_family = models.CharField(max_length=255, blank=True, verbose_name='litter or family info')
    location = models.CharField(max_length=255, blank=True, verbose_name='pets home location')
    health_rating = models.IntegerField(default=5, help_text='value 1 to 10', verbose_name='health rating #',
                                        validators=[MaxValueValidator(10),MinValueValidator(1)])
    health_status = models.CharField(max_length=255, blank=True, verbose_name='health status')
    health_issues = models.TextField(blank=True, verbose_name='known health issues')
    expired = models.DateTimeField(null=True, blank=True, verbose_name='date expired')
        
    
    def __str__(self):
            return self.name
        

