from django.shortcuts import render
from .models import*
from datetime import datetime

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
    
def todotask(request):
    print(request.POST)
    title = request.POST.get('title')
    task = request.POST.get('task')
    email = request.POST.get('email')
    # password = request.POST.get('password')
    data=RegistrationModel.objects.get(Email=email)
    taskcheck=Todolist.objects.filter(Title=title)
    if taskcheck:
        msg="This Tutle task Already Saved"  
        return render(request, 'dashboard.html', {'key1': msg, 'user_name':data})   
    else:
        Todolist.objects.create(
            Title=title,
            Task=task,
            Email=email
        )
        msg="Your Task is Saved"
        return render(request, 'dashboard.html', {'key1': msg, 'user_name':data})


# def search(request):
#     date=request.POST.get('date')
#     print(date)
#     email=request.POST.get('email')
#     print(email)
#     data=RegistrationModel.objects.get(Email=email)
#     taskdata=Todolist.objects.filter(Date=date) and Todolist.objects.filter(Email=email) 
#     # if taskdata:
#     #     return render(request, 'dashboard.html', {'user_name':data, 'tododata':taskdata})
#     # else:
#     #     msg="data not found"
#     #     return render(request, 'dashboard.html', { 'key1':msg, 'user_name':data})
#     return render(request, 'dashboard.html')


def showdata1(request, pk):
    print(pk)
    data=RegistrationModel.objects.filter(Email=pk)
    taskdata=Todolist.objects.filter(Email=pk)
    return render(request, 'dashboard.html', {'user_name':data, 'tododate':taskdata})

def showdata2(request):
    email=request.POST.get('email')
    data=RegistrationModel.objects.get(Email=email)
    taskdata=Todolist.objects.filter(Email=email)
    return render(request, 'dashboard.html', {'user_name':data, 'tododate':taskdata})


def edittodo(request, pk):
    print(pk)
    data1=Todolist.objects.get(id=pk)
    email=data1.Email
    taskdata=Todolist.objects.filter(Email=email)
    data=RegistrationModel.objects.get(Email=email)
    return render(request, 'dashboard.html', {'user_name':data, 'tododate':taskdata, 'taskobject':data1})

def delettodo(request, pk):
    print(pk)
    data=Todolist.objects.get(id=pk)
    email=data.Email
    data.delete()
    taskdata=Todolist.objects.filter(Email=email)
    data=RegistrationModel.objects.get(Email=email)
    msg="Data deleted successfully"
    return render(request, 'dashboard.html', {'user_name':data, 'tododate':taskdata, 'key1':msg})

def updatedata(request):
    pk=request.POST.get('id')
    print(request.method)
    Todotask=Todolist.objects.get(id=pk)
    email=Todotask.Email
    Todotask.id=pk
    Todotask.Title=request.POST.get('title')
    Todotask.Task=request.POST.get('task')
    Todotask.Date = datetime.now()
    Todotask.Email=request.POST.get('email')
    Todotask.save()
    taskdata=Todolist.objects.filter(Email=email)
    data=RegistrationModel.objects.get(Email=email)
    msg="Data update Successfully"
    return render(request, 'dashboard.html', {'user_name':data, 'tododate':taskdata, 'key1':msg })











