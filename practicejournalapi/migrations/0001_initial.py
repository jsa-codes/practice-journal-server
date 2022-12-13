# Generated by Django 4.1.3 on 2022-12-13 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Audio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("filename", models.FileField(max_length=254, upload_to=None)),
                ("upload_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="GuitarType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("filename", models.FileField(max_length=254, upload_to=None)),
                ("upload_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="JournalAudioUpload",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("audio", models.FileField(upload_to="")),
                ("journalentry", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="JournalComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("journalentry", models.IntegerField()),
                ("comment", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="JournalImageUpload",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.FileField(upload_to="")),
                ("journalentry", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("age", models.IntegerField(blank=True, null=True)),
                ("years_playing", models.IntegerField(blank=True, null=True)),
                ("style", models.CharField(blank=True, max_length=300, null=True)),
                (
                    "guitartype",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="practicejournalapi.guitartype",
                    ),
                ),
                (
                    "instructor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Student",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StudentGuitar",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "guitar_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="practicejournalapi.guitartype",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="practicejournalapi.student",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="JournalEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_created", models.DateField(blank=True, null=True)),
                ("time_created", models.TimeField(blank=True, null=True)),
                ("hours_slept", models.IntegerField()),
                ("water", models.IntegerField()),
                ("nutrition", models.CharField(max_length=1000)),
                ("mood", models.CharField(max_length=300)),
                ("description", models.CharField(max_length=1000)),
                ("session_length", models.FloatField()),
                (
                    "guitartype",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="practicejournalapi.guitartype",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="practicejournalapi.student",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(max_length=1000)),
                ("date_created", models.DateField(blank=True, null=True)),
                ("time_created", models.TimeField(blank=True, null=True)),
                (
                    "journalentry",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="practicejournalapi.journalentry",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
