from django.db import models

# Create your models here.
class RegistrationModel(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Number=models.IntegerField()
    Password=models.CharField(max_length=20)

    def __str__(self):
        return self.Email
    
class Todolist(models.Model):
    Title=models.CharField(max_length=200)
    Task=models.TextField()
    Date=models.DateField(auto_now=True)
    Email=models.EmailField()

    def __str__(self):
        return self.Email