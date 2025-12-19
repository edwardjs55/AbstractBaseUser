
#Using Validators (Recommended for range constraints)
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class YourModel(models.Model):
    # Field for a number between 1 and 10
    rating = models.IntegerField(
        default=5, # Optional: sets a default value
        help_text='Value between 1 and 10', # Optional: provides UI hint
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    # ... other fields


# Using IntegerChoices (Recommended for predefined options)
from django.db import models

class YourModel(models.Model):
    class NumberRange(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9
        TEN = 10

    number = models.IntegerField(choices=NumberRange.choices, default=NumberRange.ONE)
    # ... other fields
