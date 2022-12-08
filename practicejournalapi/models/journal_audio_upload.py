from django.db import models


class JournalAudioUpload(models.Model):
    audio = models.FileField()
    journalentry = models.IntegerField()
