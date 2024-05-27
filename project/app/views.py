from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import*
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from .forms import*
# from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def product(request):
    return render(request, 'product.html')

def men(request):
    data=Productmodel.objects.filter(Prod_Name="Men")
    print(data.values())
    return render(request,'men.html',{'prop':data,'media_url': settings.MEDIA_URL} )

def women(request):
    return render(request, 'women.html')

def girl(request):
    return render(request, 'girl.html')

# ================ registration function ================
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
                
                subject = 'New Customer User Account'
                message = 'A New Customer register On Our Website'+name+'  '+number+'  '+email+'  '+password
                email_from = email
                recipient_list = ['indrajeetyadu36@gmail.com', 'arpitkhare14@gmail.com','janand1997@enticerinc.onmicrosoft.com']
                send_mail(subject, message, email_from, recipient_list)
                msg="Registration Successfully Done"
                return render(request, 'login.html', {'key': msg})
            else:
                msg="Password and Confirm Password Not Match"
                return render(request, 'register.html', {'key':msg,'data1':name,'data2':email,'data3':number})


# ============= login function =====================
   
def logindata(request):
    userid=request.POST.get('userid')
    password=request.POST.get('password')
    login_type=request.POST.get('login_type')
    # print(login_type)
    username=RegistrationModel.objects.filter(Email=userid)
    if login_type=='none':
        msg="Choose your login Type"
        return render(request, 'login.html', {'key1': msg})
    elif login_type =='customer':
        if username:
            data=RegistrationModel.objects.get(Email=userid)
            print(data.Name)
            print(data)
            Password= data.Password
            if Password==password:
                msg="Welcome To "+data.Name
                return render(request, 'index.html', {'key1': msg, 'user_name':data, 'media_url':settings.MEDIA_URL})
            else:
                msg="Enter Password is Wrong Please Enter Correct Password"
                return render(request, 'login.html', {'key1': msg})
        else:
            msg="Userid doesnot exist Please create Account"
            return render(request, 'register.html', {'key1': msg})
    elif login_type =="admin":
        if username:
            data=RegistrationModel.objects.get(Email=userid)
            print(data.Name)
            print(data)
            Password= data.Password
            if Password==password:
                Context={}

                # Context['Profile']=request.session['Profile']= data.Profile
                Context['Name']=request.session['Name']= data.Name
                Context['Email']=request.session['Email']= data.Email
                Context['Number']=request.session['Number']= data.Number
                Context['Password']=request.session['Password']= data.Password
                # Context['Name']=request.session['id']= data.id
                print(data.Name)
                msg="Welcome To "+data.Name
                return render(request, 'dashboard.html', {'key1': msg, 'admin_user':data})
            else:
                msg="Enter Password is Wrong Please Enter Correct Password"
                return render(request, 'login.html', {'key1': msg})
        else:
            msg="Userid doesnot exist Please create Account"
            return render(request, 'register.html', {'key1': msg})
        

def logout(request):
    return render(request, 'index.html')

def forgetpass(request):
    return render(request, 'forgetpass.html')


def editpro(request):
    data={}
    data['Name']=request.session['Name']
    data['Email']=request.session['Email']
    data['Number']=request.session['Number']
    data['Password']=request.session['Password']

    return render(request, 'editprofile.html',{'admin_user':data})

# ======================= user Dashboard functions ===================
def home(request):
    print(request.POST)
    email=request.POST.get('email')
    data=RegistrationModel.objects.get(Email=email)
    return render(request, 'index.html', {'user_name':data})

def about1(request):
    print(request.POST)
    email=request.POST.get('email')
    data=RegistrationModel.objects.get(Email=email)
    return render(request, 'about.html', {'user_name':data})

def contact1(request):
    print(request.POST)
    email=request.POST.get('email')
    data=RegistrationModel.objects.get(Email=email)
    return render(request, 'contact.html', {'user_name':data})

def product1(request):
    print(request.POST)
    email=request.POST.get('email')
    data=RegistrationModel.objects.get(Email=email)
    return render(request, 'product.html', {'user_name':data})

def men1(request):
    print(request.POST)
    email=request.POST.get('email')
    data=RegistrationModel.objects.get(Email=email)
    data1=Productmodel.objects.filter(Prod_Name="Men")
    print(data)
    return render(request, 'men.html', {'user_name':data, 'prop':data1,'media_url': settings.MEDIA_URL})

def women1(request):
    print(request.POST)
    email=request.POST.get('email')
    data=RegistrationModel.objects.get(Email=email)
    return render(request, 'women.html', {'user_name':data})

def girl1(request):
    print(request.POST)
    email=request.POST.get('email')
    data=RegistrationModel.objects.get(Email=email)
    return render(request, 'girl.html', {'user_name':data})

# ============= user profile function -======================
def changepass(request):
    try:
        data={}
        data['Name']=request.session['Name']
        data['Email']=request.session['Email']
        data['Number']=request.session['Number']
        data['Password']=request.session['Password']
        return render(request, 'changepass.html', {'admin_user':data})
    except:
        mail=request.POST.get('email')
        dbdata=RegistrationModel.objects.get(Email=mail)
        return render(request, 'changepass.html', {'user_name':dbdata})
    
#=================== Admin dashboard ============================

def dashbordindex(request):
    data={}
    data['Name']=request.session['Name']
    data['Email']=request.session['Email']
    data['Number']=request.session['Number']
    data['Password']=request.session['Password']
    return render(request, 'dashboardindex.html', {'admin_user':data}) 

def productdata(request):
    data={}
    data['Name']=request.session['Name']
    data['Email']=request.session['Email']
    data['Number']=request.session['Number']
    data['Password']=request.session['Password']
    Context={}
    Context['prod_form']=Productmodelform
    return render(request, 'productdata.html', {'admin_user':data, 'f_content':Context})

def userdata(request):
    data={}
    data['Name']=request.session['Name']
    data['Email']=request.session['Email']
    data['Number']=request.session['Number']
    data['Password']=request.session['Password']
    return render(request, 'userdata.html', {'admin_user':data})

def result(request):
    data={}
    data['Name']=request.session['Name']
    data['Email']=request.session['Email']
    data['Number']=request.session['Number']
    data['Password']=request.session['Password']
    return render(request, 'result.html', {'admin_user':data})

def product_entry(request):
    data={}
    data['Name']=request.session['Name']
    data['Email']=request.session['Email']
    data['Number']=request.session['Number']
    data['Password']=request.session['Password']
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        serialno=request.POST.get('Serial_no')
        serialmodel=Productmodel.objects.filter(Serial_no=serialno)
        if serialmodel:
            msg = "This data already exist "
            return render(request, 'productform.html', {'msg': msg, 'admin_user':data})
        else:
            form = Productmodelform(request.POST, request.FILES)
        # print(form)
            if form.is_valid():
                form.save()
                msg = "Data submitted successfully"
                return redirect('productdata')
            else:
                msg = "There is some error, please try again"
                return render(request, 'productform.html', {'msg': msg, 'admin_user':data})
    else:
        form = Productmodelform()
        return render(request, 'productform.html', {'admin_user':data})



# ================ adminDashboard ============================  
def  todoform(request):
    data={}
    data['Name']=request.session['Name']
    data['Email']=request.session['Email']
    data['Number']=request.session['Number']
    data['Password']=request.session['Password']
    msg="open task form"
    return render(request, 'dashboard.html',{'admin_user':data, 'show':msg} )

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
        return render(request, 'dashboard.html', {'key1': msg, 'admin_user':data})   
    else:
        Todolist.objects.create(
            Title=title,
            Task=task,
            Email=email
        )
        msg="Your Task is Saved"
        return render(request, 'dashboard.html', {'key1': msg, 'admin_user':data})


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
    return render(request, 'dashboard.html', {'admin_user':data, 'tododate':taskdata})

def showdata2(request):
    email=request.POST.get('email')
    # print(email)
    data=RegistrationModel.objects.get(Email=email)
    # print(data)
    taskdata=Todolist.objects.filter(Email=email)
    # print(taskdata)
    # print(taskdata.values())
    return render(request, 'dashboard.html', {'admin_user':data, 'tododate':taskdata})


def edittodo(request, pk):
    # print(pk)
    data1=Todolist.objects.get(id=pk)
    email=data1.Email
    taskdata=Todolist.objects.filter(Email=email)
    data=RegistrationModel.objects.get(Email=email)
    return render(request, 'dashboard.html', {'admin_user':data, 'tododate':taskdata, 'taskobject':data1})

def delettodo(request, pk):
    # print(pk)
    data=Todolist.objects.get(id=pk)
    email=data.Email
    data.delete()
    taskdata=Todolist.objects.filter(Email=email)
    data=RegistrationModel.objects.get(Email=email)
    msg="Data deleted successfully"
    return render(request, 'dashboard.html', {'admin_user':data, 'tododate':taskdata, 'key1':msg})

def updatedata(request):
    Todotask=Todolist.objects.get(id=request.POST.get('id'))
    email=Todotask.Email
    Todotask.id=request.POST.get('id')
    Todotask.Title=request.POST.get('title')
    Todotask.Task=request.POST.get('task')
    Todotask.Date = datetime.now()
    Todotask.Email=request.POST.get('email')
    Todotask.save()
    taskdata=Todolist.objects.filter(Email=email)
    data=RegistrationModel.objects.get(Email=email)
    msg="Data update Successfully"
    return render(request, 'dashboard.html', {'admin_user':data, 'tododate':taskdata, 'key1':msg })






# ============ Show Product Data ================
def showmenproductdata(request):
    data=Productmodel.objects.filter(Prod_Name="women")
    print(data.values())
    return render(request,'men.html',{'prop':data,'media_url': settings.MEDIA_URL} )



# ================ Admin Product data base ==================

def product_show1(request):
    data={}
    data['Name']=request.session['Name']
    data['Email']=request.session['Email']
    data['Number']=request.session['Number']
    data['Password']=request.session['Password']
    pro_data1=Productmodel.objects.all()
    print(pro_data1.values())
    return render(request, 'productdata.html', {'admin_user':data, 'prop':pro_data1})

# =========== add To Cart functinality =========================='media_url': settings.MEDIA_URL

def addtocart(request, pk):
    email=request.POST.get('email')
    prod_name=request.POST.get('prod_name')
    if email:
        data=RegistrationModel.objects.get(Email=email)
        addtocart=request.session.get('addtocard',[])
        print(addtocart)
        if pk not in addtocart:
            addtocart.append(pk)
            print(addtocart)
        
        request.session['addtocart']=addtocart
        # addedcart={
        #     'id':id,
        #     'Email':email
        # }
        # addtocart.append(addedcart)
        addedcartno=len(addtocart)
        # return JsonResponse({'addedcartno': addedcartno})
    
    # return JsonResponse({'error': 'Email not provided'}, status=400)

        if prod_name=='Men':
            prod_data1=Productmodel.objects.filter(Prod_Name='Men')
            print(addedcartno)
            return render(request, 'men.html', {'user_name':data,'prop':prod_data1, 'addcartno':addedcartno, 'media_url': settings.MEDIA_URL})
        elif prod_name=='Women':
            prod_data1=Productmodel.objects.filter(Prod_Name='Women')
            print(addedcartno)
            return render(request, 'women.html', {'user_name':data,'prop':prod_data1, 'addcartno':addedcartno, 'media_url': settings.MEDIA_URL})
        if prod_name=='Kids':
            prod_data1=Productmodel.objects.filter(Prod_Name='Kids')
            print(addedcartno)
            return render(request, 'girl.html', {'user_name':data,'prop':prod_data1, 'addcartno':addedcartno, 'media_url': settings.MEDIA_URL})
    else:
        return redirect('login')
    
def cartpage(request):
    email=request.POST.get('email')
    data=RegistrationModel.objects.get(Email=email)
    addcart_data=request.session.get('addtocart')
    print(addcart_data)
    pro_data=[]
    for i in addcart_data: 
        pro_data.append(Productmodel.objects.get(id=i))
    cart_length=len(addcart_data)
    print(cart_length)
    print(pro_data)
    return render(request, 'addtocart.html', {'user_name':data,'prod_data':pro_data,'media_url': settings.MEDIA_URL})

        

