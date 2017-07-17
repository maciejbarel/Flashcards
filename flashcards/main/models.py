from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

# Create your models here.
class Flashcard(models.Model):
    question = models.CharField(max_length=128)
    answer = models.CharField(max_length=128)
    repeat = models.DateField(default=now)
    repeated = models.BooleanField(default=False)
    interval = models.IntegerField(default=1)
    ef = models.FloatField(default=2.5)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.question
