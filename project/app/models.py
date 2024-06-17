from django.db import models

# Create your models here.\
# ========================== 1. User Registration Model ==============================

class RegistrationModel(models.Model):
    Profile=models.ImageField(null=True, upload_to=True)
    About=models.TextField( null=True)
    Address=models.TextField( null=True)
    Username=models.CharField(max_length=20, null=True)
    Name=models.CharField(max_length=20)
    Email=models.EmailField(unique=True)
    Number=models.IntegerField()
    Password=models.CharField(max_length=20)
    Birthday=models.DateField(null=True)

    def __str__(self):
        return self.Email
    
# ========================== 2. TODO TASK MODEL ==============================

class Todolist(models.Model):
    Title=models.CharField(max_length=200)
    Task=models.TextField()
    Date=models.DateField(auto_now=True)
    Email=models.EmailField()

    def __str__(self):
        return self.Email

# ========================== 3. CAROUSEL MODEL ==============================

class IndexCarousel(models.Model):
    slide_image1 = models.ImageField(upload_to='carousel_images/')
    caption = models.CharField(max_length=250)
    cap_title = models.CharField(max_length=250)
    def __str__(self):
        return self.cap_title


# ========================== 4. MULTI IMAGE CAROUSEL MODEL ==============================

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
    

# ========================== 5. PRODUCT  ADDING MODEL ==============================

Product_for=[
    ('Men','Men'),
    ('Women','Women'),
    ('Kids','Kids'),
]
    
class Productmodel(models.Model):
    Prod_Name=models.CharField(max_length=254, null=True, choices=Product_for)
    Product_Type=models.CharField(max_length=254, null=True)
    Prod_Image1=models.ImageField(null=True)
    Prod_Image2=models.ImageField(null=True)
    Prod_Image3=models.ImageField(null=True)
    Prod_Image4=models.ImageField(null=True)
    Prod_Price =models.IntegerField(null=True)
    Prod_MRP=models.IntegerField(null=True)
    Discount=models.IntegerField(null=True)
    Prod_Offer=models.CharField(max_length=254, null=True)
    Prod_Detail=models.TextField(null=True)
    Prod_color=models.CharField(max_length=254, null=True)
    Serial_no=models.IntegerField(null=True)

    def __str__(self):
        return self.Prod_Name

# ========================== 6. PYMENT DATA MODEL ==============================


class PaymentdataModel(models.Model):
    Email=models.EmailField(null= True)
    Amount=models.IntegerField( null=True)
    Amount_paid=models.IntegerField( null=True)
    Amount_due=models.IntegerField(null=True)
    Currency=models.CharField(max_length=100, null=True)
    Receipt = models.FileField(upload_to='receipts/')
    Status=models.CharField(max_length=30, null=True)
    Attempts=models.IntegerField( null=True)
    Notes=models.TextField(null=True)
    Created_at=models.DateTimeField(auto_now=True, null=True)
    Payment_Id=models.CharField(max_length=255, null=True, blank=True)
    Order_id=models.CharField(max_length=255, null=True)
    Signature=models.CharField(max_length=255, null=True, blank=True)
    Datetime=models.DateTimeField(auto_now=True)
    Prod_Quantity=models.IntegerField( null=True)

    def __str__(self):
        return self.Order_id

# ========================== 7. PURCHASE PEODUCT DATA MODEL ==============================

class Purchaseproduct(models.Model):
    Product_Type=models.CharField(max_length=254, null=True)
    Prod_Image1=models.ImageField(null=True)
    Prod_Image2=models.ImageField(null=True)
    Prod_Image3=models.ImageField(null=True)
    Prod_Image4=models.ImageField(null=True)
    Prod_Price =models.IntegerField(null=True)
    Prod_MRP=models.IntegerField(null=True)
    Prod_Offer=models.CharField(max_length=254, null=True)
    Prod_Detail=models.TextField(null=True)
    prod_color=models.CharField(max_length=254, null=True)
    Serial_no=models.IntegerField(null=True)
    Purchase_date=models.DateTimeField(auto_now=True)
    Order_id=models.CharField(max_length=255, null=True)
    Email_id=models.EmailField(null= True)
    Prod_Quantity=models.IntegerField(null=True)

    
    def __str__(self):
        return self.Email


# ========================== 8. INVOICE DATA MODEL ==============================

class Invoicemodel(models.Model):
    Invoice_id=models.CharField(max_length=255, blank=True)
    invoice_number=models.CharField(max_length=255, blank=True)
    Customer_id=models.CharField(max_length=255, blank=True)
    Order_id=models.CharField(max_length=255, blank=True)
    Payment_id=models.CharField(max_length=255, blank=True)
    Gross_amount=models.IntegerField(blank=True)
    Tax_amount=models.IntegerField(blank=True)
    Amount=models.IntegerField(blank=True)
    Amount_paid=models.IntegerField(blank=True)
    Amount_due=models.IntegerField(blank=True)
    Currency=models.CharField(max_length=255, blank=True)
    Billing_address=models.TextField( blank=True)
    Shipping_address=models.TextField( blank=True)
    Billingtime=models.DateTimeField(auto_now=True)
    Status=models.CharField(max_length=255, blank=True)
    Invoice_pdf=models.FileField(upload_to='../invoice_pdf/', null=True)

    def __str__(self):
        return self.Customer_id


