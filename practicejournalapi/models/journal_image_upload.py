from django.db import models


class JournalImageUpload(models.Model):
    image = models.FileField()
    journalentry = models.IntegerField()
