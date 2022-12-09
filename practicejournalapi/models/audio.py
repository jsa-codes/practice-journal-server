from django.db import models


class Audio(models.Model):
    filename = models.FileField(upload_to=None, max_length=254)
    upload_date = models.DateField()
