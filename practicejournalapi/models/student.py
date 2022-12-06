from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):

    # Relationship to the built-in User model which has name and email
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    years_playing = models.IntegerField()
    style = models.CharField(max_length=300)

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
