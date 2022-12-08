from django.db import models


class JournalComment(models.Model):
    journalentry = models.IntegerField()
    comment = models.IntegerField()
