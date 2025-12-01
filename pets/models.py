# myapp/models.py
from django.db import models
# from accounts import CustomUser
from django.conf import settings


class MyPets(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user', )
    name = models.CharField(max_length=100)
    animal_type = models.CharField(max_length=100)
    description = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.name
        

