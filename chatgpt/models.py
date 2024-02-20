from django.db import models

# Create your models here.

class User(models.Model):
    userInput = models.CharField(max_length=2000)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.userInput
      
class History(models.Model):
    userInput = models.CharField(max_length=2000)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    result = models.CharField(max_length=2000)
    # type = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.userInput

class Chat(models.Model):
    userInput = models.CharField(max_length=2000)
    result = models.CharField(max_length=2000)
