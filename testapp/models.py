from django.db import models
import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=12, blank=True)
    desc = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
    