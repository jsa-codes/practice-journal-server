from django.db import models


class StudentGuitar(models.Model):
    guitar_type = models.ForeignKey("GuitarType", on_delete=models.CASCADE)
    student = models.ForeignKey(
        "Student", null=True, blank=True, on_delete=models.CASCADE)
