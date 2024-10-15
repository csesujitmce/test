from django.db import models

# Create your models here.
class BookModel(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=30)
    pages = models.IntegerField()
    price = models.FloatField()

    