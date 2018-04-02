import datetime

from django.db import models

from django.utils import timezone


# Field == Column Name, may have required arguments
# Field name [as in DB] is the Python variable name (question_text, votes, ...)
# ForeignKey relationship [M-to-M, M-to-O, O-to-O]

class Question(models.Model):
    question_text = models.CharField(max_length=300)
    publish_date = models.DateTimeField('date published')

    # Special method of Python class
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



