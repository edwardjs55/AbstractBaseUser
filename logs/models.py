from django.db import models
from pets.models import MyPets


class LogEntry(models.Model):
    pet = models.ForeignKey(MyPets, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    category = models.CharField(max_length=100, choices=[('shots', 'shots'),('spay/neuter','spay/neuter'), ('diet', 'diet'),
                                                         ('medication', 'medication'), ('other', 'other') ])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pet}: {self.action} at {self.timestamp}"
    
    