from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    date = models.DateField(null=True, blank=True,
                            auto_now=False, auto_now_add=False)
    time = models.TimeField(null=True, blank=True,
                            auto_now=False, auto_now_add=False)
