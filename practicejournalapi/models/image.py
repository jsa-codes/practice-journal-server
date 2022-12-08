from django.db import models


class Image(models.Model):
    filename = models.FileField(upload_to=None, max_length=254)
    date = models.DateField()
