from unittest.util import _MAX_LENGTH
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username= models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, default="")
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    forgot_token = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='profiles',default='media/MicrosoftTeams-image.jpeg')
                                

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
