from django.shortcuts import render
from .models import*

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def registerdata(request):
    print(request.method)
    name=request.POST.get('name')
    email=request.POST.get('email')
    print(email)
    number=request.POST.get('number')
    password=request.POST.get('password')
    con_password=request.POST.get('con_password')
    data=RegistrationModel.objects.filter(Email=email)
    if name=="" or email=="" or number=="" or password=="":
        msg="Please fill all data field"
        return render(request, 'register.html', {'key':msg,'data1':name,'data2':email,'data3':number})     
    else:
        if data:
            msg="User aleary Exist"
            return render(request, 'register.html', {'key':msg})
        else:
            if password==con_password:
                RegistrationModel.objects.create(
                    Name=name,
                    Email=email,
                    Number=number,
                    Password=password
                )
                msg="Registration Successfully Done"
                return render(request, 'login.html', {'key': msg})
            else:
                msg="Password and Confirm Password Not Match"
                return render(request, 'register.html', {'key':msg,'data1':name,'data2':email,'data3':number})
    
def logindata(request):
    # print(request.POST)
    # userid=request.POST.get('userid')
    # username=RegistrationModel.objects.filter(Email=userid)
    # return render(request, 'register.html')

    userid=request.POST.get('userid')
    password=request.POST.get('password')
    username=RegistrationModel.objects.filter(Email=userid)
    if username:
        data=RegistrationModel.objects.get(Email=userid)
        Password= data.Password
        if Password==password:
            msg="Welcome To "+data.Name
            return render(request, 'dashboard.html', {'key1': msg, 'user_name':data})
        else:
            msg="Enter Password is Wrong Please Enter Correct Password"
            return render(request, 'login.html', {'key1': msg})
    else:
        msg="Userid doesnot exist Please create Account"
        return render(request, 'register.html', {'key1': msg})

def logout(request):
    return render(request, 'home.html')


def editpro(request):
    return render(request, 'editprofile.html')
    
