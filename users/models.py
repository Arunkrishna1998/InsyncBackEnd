from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from .managers import UserAccountManager

def upload_to(instance, filename):
    return 'profile/{filename}'.format(filename=filename)

GENDER_CHOICES = [
    ('M', ('Male')),
    ('F', ('Female')),
    ('O', ('Other')),
]

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    profile_image = models.ImageField(blank=True, null=True, upload_to=upload_to, default='user.png')
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(99)])
    is_online = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    education = models.CharField(max_length=100, blank=True, null=True)
    work = models.CharField(max_length=100, blank=True, null=True)
    set_interest = models.BooleanField(default=False)
    # google_password = models.CharField(max_length=150, blank=True, null=True)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "age"]

    def __str__(self):
        return self.first_name
    
    def get_follower_count(self):
        return self.followers.count()

    def get_following_count(self):
        return self.following.count()
