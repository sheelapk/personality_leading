from django.db import models
from django.contrib.auth.models import User



class user(models.Model):
    name = models.CharField(max_length=250)
    emailid = models.EmailField()
    phone = models.CharField(max_length=11)
    message = models.TextField(max_length=500)



    def __str__(self):
        return self.emailid

