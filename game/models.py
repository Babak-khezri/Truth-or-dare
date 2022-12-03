from django.db import models

# Create your models here.

class Game(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)