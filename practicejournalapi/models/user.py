from django.db import models
from django.contrib.auth.models import User


class User(models.Model):

    # Relationship to the built-in User model which has name and email
    user = models.OneToOneField(User, on_delete=models.CASCADE)
