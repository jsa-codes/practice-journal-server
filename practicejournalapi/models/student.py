from django.db import models
from django.contrib.auth.models import User
from .guitar_type import GuitarType


class Student(models.Model):

    # Relationship to the built-in User model which has name and email
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    years_playing = models.IntegerField(null=True, blank=True)
    style = models.CharField(max_length=300, null=True, blank=True)
    guitartype = models.ForeignKey("GuitarType", on_delete=models.CASCADE)
    instructor = models.ForeignKey(
        "Instructor", null=True, blank=True, on_delete=models.CASCADE, related_name='Student')

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
