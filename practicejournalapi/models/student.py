from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):

    # Relationship to the built-in User model which has name and email
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    years_playing = models.IntegerField(null=True, blank=True)
    style = models.CharField(max_length=300, null=True, blank=True)
    instructor = models.ForeignKey(
        "Instructor", on_delete=models.CASCADE, related_name='students', null=True, blank=True)

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
