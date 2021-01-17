from django.db import models

class Contact(models.Model):
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=500)

