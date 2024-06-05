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
        fields='__all__'

class Registrationform(forms.ModelForm):
    class Meta:
        model=RegistrationModel
        fields=['Profile']
