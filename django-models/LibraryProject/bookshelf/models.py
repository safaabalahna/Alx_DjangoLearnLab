from django.db import models
# from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200),
    author = models.CharField(max_length=200),
    publication_year = models.IntegerField(),

    def __str__(self):
        return self.title