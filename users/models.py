from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    # Setting User model and Profile model one to one so that 1 user has 1 profile and vice versa
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Setting the user's profile and uploaded path
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Parent function that we making to add our own function
    def save(self, *args, **kwargs):
        # Saving image thats uploaded
        super(Profile, self).save(*args, **kwargs)

        # Grabbing the image that was just saved
        img = Image.open(self.image.path)

        # Checks if the image is bigger than x
        if img.height > 300 or img.width > 300:
            # Sets the output size
            output_size = (300, 300)
            # Re-sizes the image to the Tupal output_size
            img.thumbnail(output_size)
            # Save the image
            img.save(self.image.path)









