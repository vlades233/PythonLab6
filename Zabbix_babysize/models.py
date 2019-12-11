from django.db import models
import uuid

# Create your models here.

class Server(models.Model):
 id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text = "this is unique ID ZULUL")
 name = models.CharField(max_length=100)
 time = models.TimeField(auto_now=True)
 date = models.DateField(auto_now=True)
 ntype = models.CharField(max_length=100)
 email = models.EmailField(max_length=100)
 gtype = models.CharField(max_length=100)
 group = models.CharField(max_length=100)
 locate = models.CharField(max_length=100)

 def __str__(self):
  return self.name

class ServerCategory(models.Model):
 name = models.CharField(max_length = 100)

 def __str__(self):
   return self.name

