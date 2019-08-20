from django.db import models

# Create your models here.
class Games(models.Model):
    title = models.CharField(max_length=128)
    platform = models.CharField(max_length=128)
    score = models.CharField(max_length=128)
    genre = models.CharField(max_length=128)
    editors_choice = models.CharField(max_length=2)

    def __str__(self):
        return self.title