from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ChatGroup(models.Model):
    group_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.group_name
  
class GroupMessages(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE, related_name='chat_messages')
  body = models.CharField(max_length=300)
  created = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
     return f"{self.author.username}: {self.body}"
   
  class Meta:
    ordering = ['-created']
  