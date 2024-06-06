from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import*
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from .forms import*
from datetime import datetime
import razorpay
# from django.http import HttpResponse

# Create your views here.

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
            Context={
                 'key':msg
            }
            return render(request, 'register.html', Context)
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
                recipient_list = ['indrajeetyadu36@gmail.com']
                send_mail(subject, message, email_from, recipient_list)
                msg="Registration Successfully Done"
                return render(request, 'login.html', {'key': msg})
            else:
                msg="Password and Confirm Password Not Match"
                Context={'key':msg,
                         'data1':name,
                         'data2':email,
                         'data3':number
                         }
                return render(request, 'register.html',Context )


# ============= login function =====================
   
def logindata(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    login_type=request.POST.get('login_type')
    # print(login_type)
    username=RegistrationModel.objects.filter(Email=email)
    if login_type=='none':
        msg="Choose your login Type"
        return render(request, 'login.html', {'key1': msg})
    elif login_type =='customer':
        if username:
            data=RegistrationModel.objects.get(Email=email)
            print("*********************************************")
            
            Password= data.Password
            if Password==password:
                msg="Welcome To "+data.Name
                request.session['User_id'] = data.id
                User_id=request.session.get('User_id')
                user_info=get_object_or_404(RegistrationModel, id=User_id)
                print('user_info-->',user_info)
                Context={
                         'key1': msg, 
                         'user_name':user_info, 
                         'media_url':settings.MEDIA_URL
                        }
                return render(request, 'index.html',Context )
            else:
                msg="Enter Password is Wrong Please Enter Correct Password"
                return render(request, 'login.html', {'key1': msg})
        else:
            msg="Userid doesnot exist Please create Account"
            return render(request, 'register.html', {'key1': msg})
    elif login_type =="admin":
        if username:
            data=RegistrationModel.objects.get(Email=email)
            print(data.Name)
            print(data)
            Password= data.Password
            if Password==password:
                request.session['Admin_id'] = data.id 

                Admin_id=request.session.get('Admin_id')
                admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
                msg="Welcome To "+data.Name
                Context={
                    'media_url': settings.MEDIA_URL,
                    'key1': msg, 
                    'admin_user':admin_info 
                }
                return render(request, 'dashboard.html',Context )
            else:
                msg="Enter Password is Wrong Please Enter Correct Password"
                return render(request, 'login.html', {'key1': msg})
        else:
            msg="Userid doesnot exist Please create Account"
            return render(request, 'register.html', {'key1': msg})
        
# ============================== logout ===================================
def logout(request):
    del request.session['User_id']
    return render(request, 'index.html')

def Adminlogout(request):
    del request.session['Admin_id']
    return render(request, 'index.html')


def forgetpass(request):
    return render(request, 'forgetpass.html')

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@---- User Dashboard -----@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#====================== Starting user Dashboard (Navigation) =======================

def index(request):
    try:
        User_id=request.session.get('User_id')
        user_info=get_object_or_404(RegistrationModel, id=User_id)
        Context={
            'user_name':user_info,
            'media_url': settings.MEDIA_URL,
        }
        return render(request, 'index.html',Context )
    except:
        return render(request, 'index.html')

def about(request):
    try:
        User_id=request.session.get('User_id')
        user_info=get_object_or_404(RegistrationModel, id=User_id)
        Context={
            'user_name':user_info,
            'media_url': settings.MEDIA_URL,
        }           
        return render(request, 'about.html', Context)
    except:
        return render(request, 'about.html')

def contact(request):
    try:
        User_id=request.session.get('User_id')
        user_info=get_object_or_404(RegistrationModel, id=User_id)
        Context={
            'user_name':user_info,
            'media_url': settings.MEDIA_URL,
        }
        return render(request, 'contact.html', Context)
    except:
        return render(request, 'contact.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def product(request):
    try:
        User_id=request.session.get('User_id')
        user_info=get_object_or_404(RegistrationModel, id=User_id)
        Context={
            'user_name':user_info,
            'media_url': settings.MEDIA_URL,
        }
        return render(request, 'product.html', Context)
    except:
        return render(request, 'product.html')

# ----------------- starting Product page navigation -------------------------
def men(request):
    data=Productmodel.objects.filter(Prod_Name="Men")
    print(data.values()) 
    try:
        User_id=request.session.get('User_id')
        user_info=get_object_or_404(RegistrationModel, id=User_id)
        Context={
            'prop':data,
            'media_url': settings.MEDIA_URL,
            'user_name':user_info
        }
        return render(request, 'men.html',Context)
    except:
        Context={
            'prop':data,
            'media_url': settings.MEDIA_URL
        }
        return render(request,'men.html',Context )


def women(request):
    data=Productmodel.objects.filter(Prod_Name="Men")
    print(data.values())
    try:
        User_id=request.session.get('User_id')
        user_info=get_object_or_404(RegistrationModel, id=User_id)
        Context={
        'prop':data,
        'media_url': settings.MEDIA_URL,
        'user_name':user_info
    }
        return render(request, 'women.html', Context)
    except:
        Context={
        'prop':data,
        'media_url': settings.MEDIA_URL
    }
        return render(request, 'women.html',Context)

def girl(request):
    data=Productmodel.objects.filter(Prod_Name="Girl")
    # print(data.values())
    try:
        User_id=request.session.get('User_id')
        user_info=get_object_or_404(RegistrationModel, id=User_id)
        Context={
        'prop':data,
        'media_url': settings.MEDIA_URL,
        'user_name':user_info
    }
        return render(request, 'girl.html', Context )
    except:
        Context={
            'prop':data,
            'media_url': settings.MEDIA_URL
        }
        return render(request, 'girl.html', Context)
    
# ====================== Starting User Dashboard (Add to Cart) =============================================
#  =---------------------- Starting Cart add Button -----------------------------------------------
def addtocart(request, pk):
    # user_info=request.session.get('user_info')
    email = request.POST.get('email')
    prod_name = request.POST.get('prod_name')
    if email:
        data = RegistrationModel.objects.get(Email=email)
        addtocart = request.session.get('addtocart', [])
        if pk not in [item['id'] for item in addtocart]:
            add_cartdata = {
                'id': pk,
                'Quantity': 1
            }
            addtocart.append(add_cartdata)
        request.session['addtocart'] = addtocart
        addedcartno = len(addtocart)
        user_info=data
        if prod_name == 'Men':
            prod_data1 = Productmodel.objects.filter(Prod_Name='Men')
            Context={
                'user_name': user_info, 
                'prop': prod_data1, 
                'addcartno': addedcartno, 
                'media_url': settings.MEDIA_URL
            }
            return render(request, 'men.html', Context)
        elif prod_name == 'Women':
            prod_data1 = Productmodel.objects.filter(Prod_Name='Women')
            Context={
                'user_name': user_info, 
                'prop': prod_data1, 
                'addcartno': addedcartno, 
                'media_url': settings.MEDIA_URL
            }
            return render(request, 'women.html', Context)
        elif prod_name == 'Kids':
            prod_data1 = Productmodel.objects.filter(Prod_Name='Kids')
            Context={
                'user_name': user_info, 
                'prop': prod_data1, 
                'addcartno': addedcartno, 
                'media_url': settings.MEDIA_URL
            }
            return render(request, 'girl.html', Context)
    else:
        return redirect('login')
    
#  =---------------------- ENDing Cart add Button -----------------------------------------------

def cartpage(request):
    # email = request.POST.get('email')
    # data = RegistrationModel.objects.get(Email=email)
    User_id=request.session.get('User_id')
    user_info=get_object_or_404(RegistrationModel, id=User_id)
    try:
        addcart_data = request.session.get('addtocart', [])
        # print(addcartround(_data)
        total_MRP = 0
        total_amount = 0
        tax = 0
        shippingcharge = 40
        Quantity=0
        pro_data = []
        for item in addcart_data:
            # print(item)
            pro_value = Productmodel.objects.get(id=item['id'])
            # print(pro_value)
            pro_quantitydata = {
                'pro_value': pro_value,
                'Quantity': item['Quantity']
            }
            pro_data.append(pro_quantitydata)
            # print(pro_quantitydata)
            total_amount += pro_value.Prod_Price * item['Quantity']
            total_MRP += pro_value.Prod_MRP * item['Quantity']
            tax += int(round((total_amount * 12) / 100,0))
            Quantity += item['Quantity']

        discount = total_MRP - total_amount
        Total_pay_amount = total_amount + shippingcharge + tax

        billamount = {
            'total_amount': total_amount,
            'total_MRP': total_MRP,
            'discount': discount,
            'tax': tax,
            'shippingcharge': shippingcharge,
            'Total_pay_amount': Total_pay_amount,
            'Quantity':Quantity     
        }
        Context={
            'user_name': user_info, 
            'prod_data': pro_data, 
            'media_url': settings.MEDIA_URL, 
            'amount': billamount
        }
        return render(request, 'addtocart.html', Context)
    except:
        return render(request, 'login.html')


# ====================== Ending User Dashboard (Add to Cart) =============================================
 
# ======================== Starting user profile Function ==========================================

def editpro(request):
    email=request.POST.get('email')
    Account_type=request.POST.get('accounttype')
    if Account_type=='admin_profile':
        Admin_id=request.session.get('Admin_id')
        admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
        Context={
            'admin_user':admin_info,
            'profileform':Registrationform,
            'media_url': settings.MEDIA_URL, 
        }
        return render(request, 'editprofile.html', Context)
    elif Account_type=='user_profile':
        User_id=request.session.get('User_id')
        user_info=get_object_or_404(RegistrationModel, id=User_id)
        Context={
            'user_name': user_info,
            'profileform':Registrationform,
            'media_url': settings.MEDIA_URL, 
        }
        return render(request, 'editprofile.html', Context)
    
# -------------- image updating -------------------
def updatepro_img(request):
    profile_img=request.FILES.get('Profile')
    print(profile_img)
    pro_image=request.POST.get('Profile')
    Account_type=request.POST.get('accounttype')
    print(Account_type)
    if Account_type =='user_profile':
        User_id=request.session.get('User_id')
        user_info=get_object_or_404(RegistrationModel, id=User_id)
        regist= RegistrationModel.objects.get(Email=user_info.Email)
        print(regist)
        regist.Profile=profile_img
        regist.save(update_fields=['Profile'])
        data=get_object_or_404(RegistrationModel, Email=user_info.Email)
        Context={
            'user_name' : user_info,
            'media_url': settings.MEDIA_URL,
            'profileform':Registrationform
        }
        return render(request, 'editprofile.html', Context)
    if Account_type =='admin_profile':
        Admin_id=request.session.get('Admin_id')
        admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
        regist=get_object_or_404(RegistrationModel, Email=admin_info.Email)
        print(regist)
        regist.Profile = pro_image
        regist.save(update_fields=['Profile'])
        registdata=get_object_or_404(RegistrationModel, Email=admin_info.Email)
        print(registdata)
        Context={
            'user_name' : registdata,
            'media_url': settings.MEDIA_URL,
            'profileform':Registrationform
        }
        return render(request, 'editprofile.html',Context )

def userprofile(request):
    User_id=request.session.get('User_id')
    User_info=get_object_or_404(RegistrationModel, id=User_id)
    username=request.POST.get('username')
    Fname=request.POST.get('Fname')
    address=request.POST.get('address')
    about=request.POST.get('about')
    email=request.POST.get('email')
    number=request.POST.get('number')
    birthday=request.POST.get('birthday')

    User_info.About=about
    User_info.Username=username
    User_info.Name=Fname
    User_info.Address=address
    User_info.Email=email
    User_info.Number=number
    User_info.Birthday=birthday
    User_info.save(update_fields=['About','Username','Name','Email','Number','Birthday', 'Address'])
    user_info=get_object_or_404(RegistrationModel, id=User_id)
    Context={
       'user_name' : user_info,
        'media_url': settings.MEDIA_URL, 
    }
    return render(request, 'editprofile.html',Context)

# --------------------------------------------

def changepass(request):
    try:
        Admin_id=request.session.get('Admin_id')
        admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
        Context={
            'admin_user':user_info,
            'media_url': settings.MEDIA_URL
        }
        return render(request, 'changepass.html', {'admin_user':admin_info})
    except:
        User_id=request.session.get('User_id')
        user_info=get_object_or_404(RegistrationModel, id=User_id)
        Context={
            'user_name':user_info,
            'media_url': settings.MEDIA_URL,
        }
        return render(request, 'changepass.html', Context)


def passwordchange(request):
    if request.method=='POST':
        email=request.POST.get('email')
        print(email)
        login_type=request.POST.get('login_type')
        newpassword=request.POST.get('newpassword')
        conpassword=request.POST.get('conpassword')
        register = get_object_or_404(RegistrationModel, Email=email)
    try:
        if newpassword == conpassword:
            print(register)
            register.Password = newpassword
            register.save(update_fields=['Password'])

            msg="Password successfully Changed"
            User_id=request.session.get('User_id')
            user_info=get_object_or_404(RegistrationModel, id=User_id)
            Context={
                'key':msg,
                'user_name':user_info,
                'media_url': settings.MEDIA_URL, 
            }    
            return render(request, 'index.html',Context)
    except:

        if newpassword == conpassword:
            register.Password = newpassword
            register.save(update_fields=['Password'])
            request.session['Password']=newpassword
            msg="Password successfully Changed"

        Admin_id=request.session.get('Admin_id')
        admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
        Context={
            'key':msg,
            'admin_user':admin_info,
             'media_url': settings.MEDIA_URL
        }
        return render(request, 'dashboard.html', Context)    

    
#========================= Endinging user profile Function ==========================================
#========================= ENDing user Dashboard (Navigation) ========================================

# ============ Show Product Data ================
def showmenproductdata(request):
    data=Productmodel.objects.filter(Prod_Name="women")
    # print(data.values())
    return render(request,'men.html',{'prop':data,'media_url': settings.MEDIA_URL} )



# =================== Startinging User Dashboard (Razorpay payment integrations) ================================

def checkout(request):
    amount=int(request.POST.get('amount'))*100
    # print(amount)
    email=request.POST.get('email')
    # print(email)
    userdata=RegistrationModel.objects.get(Email=email)
    global Payableamount 
    # amount in paisa
    client = razorpay.Client(auth =("rzp_test_8jTLUV3aVex82Q" , "n3PL7ZbSgnKSWJeA1s9ndhaO"))
    # amount = int(amount * 100)
    #create order
    data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11" }
    # print(data)
    payment = client.order.create(data=data)
    print("Payment ----->",payment)
    Payableamount=payment

    print(payment['id'])
    PaymentdataModel.objects.create(
        Email=email,
        Amount=payment['amount'],
        Amount_paid=payment['amount_paid'],
        Amount_due=payment['amount_due'],
        Currency=payment['currency'],
        Receipt =payment['receipt'],
        Status=payment['status'],
        Attempts=payment['attempts'],
        Notes=payment['notes'],
        Created_at=payment['created_at'], 
        Order_id=payment['id']
    )
    addcart_data = request.session.get('addtocart', [])
    # print(addcartround(_data)
    total_MRP = 0
    total_amount = 0
    tax = 0
    shippingcharge = 40
    Quantity=0
    pro_data = []

    for item in addcart_data:
        # print(item)
        pro_value = Productmodel.objects.get(id=item['id'])
        # print(pro_value)
        pro_quantitydata = {
            'pro_value': pro_value,
            'Quantity': item['Quantity']
        }
        pro_data.append(pro_quantitydata)
        # print(pro_quantitydata)
        total_amount += pro_value.Prod_Price * item['Quantity']
        total_MRP += pro_value.Prod_MRP * item['Quantity']
        tax += int(round((total_amount * 12) / 100,2))
        Quantity += item['Quantity']

    discount = total_MRP - total_amount
    Total_pay_amount = total_amount + shippingcharge + tax
    
    billamount = {
        'total_amount': total_amount,
        'total_MRP': total_MRP,
        'discount': discount,
        'tax': tax,
        'shippingcharge': shippingcharge,
        'Total_pay_amount': Total_pay_amount,
        'Quantity':Quantity
    }

    cart_length = len(addcart_data)
    user_info=request.session.get('user_info')
    Context={
        'user_name': user_info, 
        'pay_data':data, 
        'media_url': settings.MEDIA_URL,
        'payment':payment,
        'amount': billamount,
        'prod_data': pro_data,
        'length':cart_length
    }
    # print(payment)
    return render(request, 'addtocart.html', Context)
#  -------------------- MakePayment -----------------------------------
@csrf_exempt
def making_payment(request):
    print('******************')
    # print(request.POST)
    razorpay_payment_id = request.POST.get('razorpay_payment_id')
    razorpay_order_id = request.POST.get('razorpay_order_id')
    email = request.POST.get('email')
    print(razorpay_order_id)
    razorpay_signature = request.POST.get('razorpay_signature')
    payment_data= get_object_or_404(PaymentdataModel, Order_id=razorpay_order_id)
    print(payment_data)
    payment_data.Payment_Id = razorpay_payment_id
    payment_data.Signature = razorpay_signature
    
    user_info=request.session.get('user_info')
    # Save the updated payment data
    payment_data.save(update_fields=['Payment_Id', 'Signature'])
    if 'addtocart' in request.session:
        del request.session['addtocart']
    print(user_info)
    Context={
         'user_name': user_info,
         'media_url': settings.MEDIA_URL, 
    }
    return render(request, 'paymentdone.html', Context)

# ====================== Ending User Dashboard (Razorpay payment integrations) ======================================



# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  Admin Dashboard Views Function @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    #===================Starting Admin dashboard (Navigation)============================

def dashbordindex(request):
    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    Context={
        'media_url': settings.MEDIA_URL,
        'admin_user':admin_info
    }
    return render(request, 'dashboardindex.html', Context) 

def productdata(request):
    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    Context={
        'admin_user':admin_info,    
        'prod_form':Productmodelform,
        'media_url': settings.MEDIA_URL,
    }
    
    return render(request, 'productdata.html',Context )

def userdata(request):
    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    Context={
        'media_url': settings.MEDIA_URL,
        'admin_user':admin_info
    }
    return render(request, 'userdata.html', Context)

def result(request):
    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    Context={
        'media_url': settings.MEDIA_URL,
        'admin_user':admin_info
    }
    return render(request, 'result.html', {'admin_user':admin_info})

def product_entry(request):
    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    if request.method == "POST":
        # print(request.POST)
        # print(request.FILES)
        serialno=request.POST.get('Serial_no')
        serialmodel=Productmodel.objects.filter(Serial_no=serialno)
        if serialmodel:
            msg = "This data already exist "
            Context={
                    'media_url': settings.MEDIA_URL,
                    'admin_user':admin_info,
                    'msg': msg,
                }
            return render(request, 'productform.html', Context)
        else:
            form = Productmodelform(request.POST, request.FILES)
        # print(form)
            if form.is_valid():
                form.save()
                msg = "Data submitted successfully"
                return redirect('productdata')
            else:
                msg = "There is some error, please try again"
                Context={
                    'media_url': settings.MEDIA_URL,
                    'admin_user':admin_info,
                    'msg': msg,
                }
                return render(request, 'productform.html', Context)
    else:
        form = Productmodelform()
        Context={
        'media_url': settings.MEDIA_URL,
        'admin_user':admin_info
        }
        return render(request, 'productform.html', Context)
    
#======================= ENDing Admin dashboard (Navigation) =================================
    
# ====================== Starting admin Dashboard (Todo task CRUD) ============================  
def  todoform(request):
    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    msg="open task form"
    return render(request, 'dashboard.html',{'admin_user':admin_info, 'show':msg} )

def todotask(request):
    # print(request.POST)
    title = request.POST.get('title')
    task = request.POST.get('task')
    email = request.POST.get('email')

    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    
    taskcheck=Todolist.objects.filter(Title=title)
    if taskcheck:
        msg="This Tutle task Already Saved"  
        return render(request, 'dashboard.html', {'key1': msg, 'admin_user':admin_info})   
    else:
        Todolist.objects.create(
            Title=title,
            Task=task,
            Email=email
        )
        msg="Your Task is Saved"
        return render(request, 'dashboard.html', {'key1': msg, 'admin_user':admin_info})


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
    
    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    taskdata=Todolist.objects.filter(Email=admin_info.Email)
    return render(request, 'dashboard.html', {'admin_user':admin_info, 'tododate':taskdata})

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

# ========================= ENDing admin Dashboard (Todo task CRUD) =======================================

# ========================= Starting Admin Dashboard (Product CRUD) ========================================

def product_show1(request):
    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    pro_data1=Productmodel.objects.all()
    print(pro_data1.values())
    Context={
        'admin_user':admin_info, 
        'prop':pro_data1, 
        'media_url': settings.MEDIA_URL
    }
    return render(request, 'productdata.html', Context)

# ================ ENDing Admin Dashboard (Product CRUD) ======================

#=================== User Dashboard login after Navition =============
# def home(request):
#     return render(request, 'index.html', {'user_name':user_info})

# def about1(request):
#     print(request.POST)
#     email=request.POST.get('email')
#     data=RegistrationModel.objects.get(Email=email)
#     return render(request, 'about.html', {'user_name':user_info})

# def contact1(request):
#     print(request.POST)
#     email=request.POST.get('email')
#     data=RegistrationModel.objects.get(Email=email)
#     return render(request, 'contact.html', {'user_name':user_info})

# def product1(request):
#     print(request.POST)
#     email=request.POST.get('email')
#     data=RegistrationModel.objects.get(Email=email)
#     return render(request, 'product.html', {'user_name':user_info})

# def men1(request):
#     print(request.POST)
#     email=request.POST.get('email')
#     data=RegistrationModel.objects.get(Email=email)
#     data1=Productmodel.objects.filter(Prod_Name="Men")
#     print(data)
#     Context={
#         'user_name':user_info, 
#         'prop':data1,
#         'media_url': settings.MEDIA_URL
#     }
#     return render(request, 'men.html',Context )

# def women1(request):
#     print(request.POST)
#     email=request.POST.get('email')
#     data=RegistrationModel.objects.get(Email=email)
#     return render(request, 'women.html', {'user_name':user_info})

# def girl1(request):
#     print(request.POST)
#     email=request.POST.get('email')
#     data=RegistrationModel.objects.get(Email=email)
#     return render(request, 'girl.html', {'user_name':user_info})