from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # Setting User model and Profile model one to one so that 1 user has 1 profile and vice versa
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Setting the user's profile and uploaded path
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
