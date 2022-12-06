from django.db import models


class JournalComment(models.Model):
    journal_entry = models.IntegerField()
    comment = models.IntegerField()
