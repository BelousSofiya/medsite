from django.db import models


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    source_link = models.URLField(max_length=128, db_index=True, blank=True)
    date_of_publishing = models.DateField()
    date_on_site = models.DateField(auto_now_add=True)
    authors = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
