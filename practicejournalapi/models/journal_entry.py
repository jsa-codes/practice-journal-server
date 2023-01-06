from django.db import models


class JournalEntry(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE)

    date = models.DateField(null=True, blank=True,
                            auto_now=False, auto_now_add=False)

    time = models.TimeField(null=True, blank=True,
                            auto_now=False, auto_now_add=False)
    hours_slept = models.IntegerField()
    water = models.IntegerField()
    nutrition = models.CharField(max_length=1000)
    mood = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    session_length = models.FloatField()
