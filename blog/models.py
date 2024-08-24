from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True, blank=True)

    def __str__(self):
        return self.user.username
