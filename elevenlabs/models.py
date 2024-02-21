from django.db import models

# Create your models here.


class ElevenData(models.Model):
    input_text = models.CharField(max_length=2500)
    date_text = models.CharField(max_length=2500)

    def __str__(self):
        return self.input_text
