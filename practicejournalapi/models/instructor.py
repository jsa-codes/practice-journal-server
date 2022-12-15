from django.db import models
from django.contrib.auth.models import User


class Instructor(models.Model):

    # Relationship to the built-in User model which has name and email
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    years_playing = models.IntegerField(null=True, blank=True)
    bio = models.CharField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=35, null=True, blank=True)

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
