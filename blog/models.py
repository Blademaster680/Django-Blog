from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    # If the user is deleted we want to delete their posts as well. 'on_delete=models.CASCADE'
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title