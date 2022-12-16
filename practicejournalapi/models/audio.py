from django.db import models


class Audio(models.Model):
    filename = models.FileField(upload_to=None, max_length=254)
    upload_date = models.DateField(null=True, blank=True,
                                   auto_now=False, auto_now_add=False)
