from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150, default='anonymous')
    genre = models.CharField(max_length=100)
    height = models.IntegerField()
    publisher = models.CharField(max_length=100)
    # Add more fields as required

    def __str__(self):
        return self.title