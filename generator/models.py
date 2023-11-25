from django.db import models

class Question(models.Model):
    question_text = models.TextField()
    subject = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=10)
    marks = models.IntegerField()

    def __str__(self):
        return self.question_text