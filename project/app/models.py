from django.db import models

# Create your models here.
class RegistrationModel(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Number=models.IntegerField()
    Password=models.CharField(max_length=20)

    def __str__(self):
        return