from django import forms
from .models import*

class indexcarouselform(forms.ModelForm):
    class Meta:
        model=IndexCarousel
        fields='__all__'

class ProductBoxform(forms.ModelForm):
    class Meta:
        model=ProductBox
        fields='__all__'


class Productmodelform(forms.ModelForm):
    class Meta:
        model=Productmodel
        fields=['Prod_Name','Product_Type',
                'Prod_Image1','Prod_Image2', 
                'Prod_Image3', 'Prod_Image4',
                'Prod_MRP','Prod_Offer','Prod_Detail',
                'Prod_color','Serial_no'
                ]

class Registrationform(forms.ModelForm):
    class Meta:
        model=RegistrationModel
        fields=['Profile']

class RegistrationDataform(forms.ModelForm):
    class Meta:
        model=RegistrationModel
        fields='__all__'

class RegistrationDataform(forms.ModelForm):
    class Meta:
        model=RegistrationModel
        fields='__all__'





