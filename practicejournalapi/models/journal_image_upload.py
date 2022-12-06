from django.db import models


class JournalImageUpload(models.Model):
    image = models.FileField()
    journal_entry = models.IntegerField()
