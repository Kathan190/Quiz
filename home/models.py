from django.db import models

# Create your models here.

class Signup(models.Model):
    email = models.CharField(max_length=150, default='')
    psw = models.CharField(max_length=150, default='')
    psw_repeat = models.CharField(max_length=150,default='')

    def __str__(self):
        return self.email

class Contact(models.Model):
    email = models.CharField(max_length=150, default='')
    contact = models.CharField(max_length=20)
    subject = models.TextField()

    def __str__(self):
        return self.email + ' ' + self.contact + ' ' + self.subject

class Login(models.Model):
    email = models.CharField(max_length=150, default='')
    psw = models.CharField(max_length=150)

    def __str__(self):
        return self.email
    
    