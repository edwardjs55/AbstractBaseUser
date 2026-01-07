from django.conf import settings
from django.db import models

# Create your models here.

class Agency(models.Model):
    director = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100, blank=True)
    contact_email = models.EmailField(blank=True)   
    location = models.CharField(max_length=255, blank=True)    
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    started = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    staff = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='agency_staff', blank=True)
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('agency_detail', args=[str(self.id)]) 


    def __str__(self):
        return self.name    
    