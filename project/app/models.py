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

class IndexCarousel(models.Model):
    slide_image1 = models.ImageField(upload_to='carousel_images/')
    caption = models.CharField(max_length=250)
    cap_title = models.CharField(max_length=250)
    def __str__(self):
        return self.cap_title

class ProductBox(models.Model):
    heading = models.CharField(max_length=250)
    image1 = models.ImageField(upload_to='product_images/')
    image2 = models.ImageField(upload_to='product_images/')
    image3 = models.ImageField(upload_to='product_images/')
    image4 = models.ImageField(upload_to='product_images/')
    image_title1 = models.CharField(max_length=250)
    image_title2 = models.CharField(max_length=250)
    image_title3 = models.CharField(max_length=250)
    image_title4 = models.CharField(max_length=250)

    def get_heading(self):
        return self.heading

