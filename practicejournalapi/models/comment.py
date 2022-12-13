from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    journalentry = models.ForeignKey(
        "JournalEntry", on_delete=models.CASCADE, related_name='comments')
    description = models.CharField(max_length=1000)
    date_created = models.DateField(null=True, blank=True,
                                    auto_now=False, auto_now_add=False)
    time_created = models.TimeField(null=True, blank=True,
                                    auto_now=False, auto_now_add=False)
