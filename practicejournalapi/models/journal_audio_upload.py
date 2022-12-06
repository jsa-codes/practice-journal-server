from django.db import models


class JournalAudioUpload(models.Model):
    audio = models.FileField()
    journal_entry = models.IntegerField()
