from django.db import models


class GuitarType(models.Model):
    type = models.CharField(max_length=155)
