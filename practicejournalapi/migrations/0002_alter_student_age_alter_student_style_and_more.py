# Generated by Django 4.1.3 on 2022-12-06 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("practicejournalapi", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="age",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="style",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="years_playing",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]