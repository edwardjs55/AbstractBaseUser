
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import login
from django.shortcuts import render, redirect

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        # return self.mylogin(self.user)
        return user
    
    def mylogin(request,user):
        login(request,user)
        return redirect('home')

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    # Add any other custom fields you need
    username = models.CharField(unique=False,null=True,blank=True,max_length=150,verbose_name='username')
    first_name = models.CharField(unique=False,null=True,blank=True,max_length=150,verbose_name='first name')
    last_name = models.CharField(unique=False,null=True,blank=True,max_length=150,verbose_name='last name')
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = [] # Add other required fields here if any

    def __str__(self):
        return self.email  

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    