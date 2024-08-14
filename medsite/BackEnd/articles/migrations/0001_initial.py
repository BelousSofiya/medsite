# Generated by Django 4.2.3 on 2023-09-15 12:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=50)),
                ("content", models.TextField()),
                (
                    "source_link",
                    models.URLField(blank=True, db_index=True, max_length=128),
                ),
                ("date_of_publishing", models.DateField()),
                ("date_on_site", models.DateField(auto_now_add=True)),
                ("authors", models.CharField(max_length=250)),
                ("description", models.CharField(max_length=250)),
            ],
        ),
    ]