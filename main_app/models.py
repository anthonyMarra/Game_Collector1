# Create your models here.
from django.db import models
from django.urls import reverse


# Create your models here.
class Game(models.Model):
  # define the fields/columns
  name = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  hoursPlayed = models.IntegerField()

  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('game_detail', kwargs={'game_id': self.id})