from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Question(models.Model):
    RATING = 1
    PLANTEXT = 2
    TYPES = ((RATING,'Rating'),(PLANTEXT,'PlanText'),)
    question = models.CharField(max_length=500)
    types = models.IntegerField(choices=TYPES, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.question} "
class Answer(models.Model):
    user_session = models.CharField(max_length=150)
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.question.question} {self.answer}"
    
    class Meta:
        unique_together = ('user_session', 'question')
                                                           
