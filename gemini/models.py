from django.db import models


class Gemini(models.Model):
    userInput = models.CharField(max_length=2000)
    result = models.CharField(max_length=2000) 