from django.db import models


class Audio(models.Model):
    file_name = models.FileField(upload_to=None, max_length=254)
    date = models.DateField()
