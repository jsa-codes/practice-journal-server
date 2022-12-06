from django.db import models
from django.contrib.auth.models import User


class JournalEntry(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True,
                            auto_now=False, auto_now_add=False)

    time = models.DateField(null=True, blank=True,
                            auto_now=False, auto_now_add=False)
    hours_slept = models.IntegerField()
    water_intake = models.IntegerField()
    nutrition = models.CharField(max_length=1000)
    mood = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    session_length = models.FloatField()
