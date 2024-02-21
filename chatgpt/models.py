from django.db import models

class ChatUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class ChatHistory(models.Model):
    user = models.ForeignKey(ChatUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()  

    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"

class ChatResponse(models.Model):
    history = models.ForeignKey(ChatHistory, on_delete=models.CASCADE, related_name='responses')  # One-to-many
    response_message = models.TextField()  

    def __str__(self):
        return f"Response to {self.history.user.username} at {self.history.timestamp}"
