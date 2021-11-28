from django.db import models


class Book (models.Model):
    title_book = models.CharField(max_length=100)
    authors = models.CharField(max_length=50)
    publishedData = models.DateTimeField()
    type = models.CharField(max_length=30)
    pageCount = models.CharField(max_length=5)
    selfLink = models.CharField(max_length=200)
    language = models.CharField(max_length=20)
