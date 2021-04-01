from django.db import models

# Create your models here.

class Signup(models.Model):
    email = models.CharField(max_length=150)
    psw = models.CharField(max_length=150)
    psw_repeat = models.CharField(max_length=150)

    def __str__(self):
        return self.email