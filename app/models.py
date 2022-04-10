from email import message
from django.db import models

# Create your models here.
class Info(models.Model):
     file_name=models.CharField(max_length=500)
     chat_id=models.IntegerField()
     message_id=models.IntegerField()
     def __str__(self):
          return self.file_name