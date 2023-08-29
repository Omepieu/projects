from django.db import models
import datetime
from django.utils import timezone

from django.contrib import admin


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200) #champs de type chaine de caractère
    pub_date = models.DateTimeField("date de publication") #champs de type date et l'heure

    def __str__(self):
        return self.question_text
    
    def date_publier_plus_recent(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    @admin.display(
            boolean=True,
            ordering = 'pub_date',
            description = 'Publiée recement'
    )
    def fut_publier_recent(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choix(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choix_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choix_text
    
