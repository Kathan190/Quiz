from django.db import models

# Create your models here.

class Contact(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    subject = models.TextField()

    def __str__(self):
        return self.firstname