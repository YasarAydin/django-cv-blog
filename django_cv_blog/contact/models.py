from django.db import models


# Create your models here.

class Contact(models.Model):
    your_firstname = models.CharField(max_length=50)
    your_lastname = models.CharField(max_length=50)
    your_email = models.EmailField()
    your_message = models.TextField()
