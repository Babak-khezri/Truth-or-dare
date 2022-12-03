from django.db import models

# Create your models here.


class Question(models.Model):
    DIFICALLITY_CHOICES = (
        ('e', 'easy'), ('m', 'medium'), ('d', 'dificial')
    )
    CATEGORY_CHOICES = (('d', 'dare'), ('t', 'truth'))
    text = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    dificallity = models.CharField(max_length=1, choices=DIFICALLITY_CHOICES)
    is_rude = models.BooleanField(default=False)
    is_proved = models.BooleanField(default=False)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.text
