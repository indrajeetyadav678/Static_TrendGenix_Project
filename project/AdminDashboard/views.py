from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse,FileResponse
from .models import*
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from app.forms import*
from datetime import datetime
import string
import random
# from django.http import HttpResponse

# Create your views here.

#===================Starting Admin dashboard (Navigation)============================
def Adminlogout(request):
    del request.session['Admin_id']
    return render(request, 'index.html')

def dashbordindex(request):
    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    customer_data=RegistrationModel.objects.all()
    total_customer_quantity=len(customer_data)
    invoice_data=Invoicemodel.objects.all()
    global total_sell
    total_sell=0
    for i in invoice_data:
        total_sell+=i.Amount_paid

    print(customer_data)
    Context={
        'media_url': settings.MEDIA_URL,
        'admin_user':admin_info,
        'customer':customer_data,
        "customer_no":total_customer_quantity,
        'monthly_sell':total_sell
    }
    return render(request, 'dashboardindex.html', Context) 
# ------------------------ register data CRUD -----------------------
def editregistdata(request, pk):
    data=RegistrationModel.objects.get(id=pk)
    
    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    customer_data=RegistrationModel.objects.all()
    total_customer_quantity=len(customer_data)
    print(customer_data)
    Context={
        'media_url': settings.MEDIA_URL,
        'admin_user':admin_info,
        'customer':customer_data,
        'registform':Registrationform,
        'editdata':data,
        "customer_no":total_customer_quantity,
        'monthly_sell':total_sell
    }
    return render(request, 'dashboardindex.html', Context)

def deletregistdata(request, pk):
    data=RegistrationModel.objects.get(id=pk)
    data.delete()
    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    customer_data=RegistrationModel.objects.all()
    total_customer_quantity=len(customer_data)
    print(customer_data)
    Context={
        'media_url': settings.MEDIA_URL,
        'admin_user':admin_info,
        'customer':customer_data,
        "customer_no":total_customer_quantity,
        'monthly_sell':total_sell
    }
    return render(request, 'dashboardindex.html', Context)



def updateeditregistdata(request):
    print(request.FILES)
    print(request.POST)


    data=RegistrationModel.objects.get(Email=request.POST['email'])
    data.Profile=request.FILES.get('profile')
    data.Name=request.POST['name']
    data.Username=request.POST['username']
    data.Email=request.POST['email']
    data.Address=request.POST['address']
    data.Number=request.POST['number']
    data.Password=request.POST['password']
    data.Birthday=request.POST['birthday']
    data.About=request.POST['about']
    data.save()
    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    customer_data=RegistrationModel.objects.all()
    total_customer_quantity=len(customer_data)

    print(customer_data)
    Context={
        'media_url': settings.MEDIA_URL,
        'admin_user':admin_info,
        'customer':customer_data,
        'key':'Data Suceesfully Updated',
        "customer_no":total_customer_quantity,
        'monthly_sell':total_sell
    }
    return render(request, 'dashboardindex.html', Context)


# =============== completed Registrationt data CRUD =====================
# =============== Starting Product data CRUD ===========================

def productdata(request):
    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    data=Productmodel.objects.all()
    Context={
        'admin_user':admin_info,    
        'prod_form':Productmodelform,
        'media_url': settings.MEDIA_URL,
        'prop':data
    }
    
    return render(request, 'productdata.html',Context )
# -------------- product dtat CRUD -------------------------
def editproductdata(request, pk):
    data=Productmodel.objects.get(id=pk)
    
    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    product_data=Productmodel.objects.all()
    print(product_data)
    Context={
        'media_url': settings.MEDIA_URL,
        'admin_user':admin_info,
        'prop':product_data,
        'Productdataform':Productmodelform,
        'editdata':data
    }
    return render(request, 'productdata.html', Context)

def deletproductdata(request, pk):
    print(pk)
    data=Productmodel.objects.get(id=pk)
    data.delete()
    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    product_data=Productmodel.objects.all()
    print(product_data)
    Context={
        'media_url': settings.MEDIA_URL,
        'admin_user':admin_info,
        'prop':product_data,
        'key':'Data Successfully Deleted'
    }
    return render(request, 'productdata.html', Context)



def updateditproductdata(request):
    print(request.FILES)
    print(request.POST)
    data=Productmodel.objects.get(id=request.POST['id'])
    data.Profile=request.FILES.get('profile')
    data.Name=request.POST['name']
    data.Username=request.POST['username']
    data.Email=request.POST['email']
    data.Address=request.POST['address']
    data.Number=request.POST['number']
    data.Password=request.POST['password']
    data.Birthday=request.POST['birthday']
    data.About=request.POST['about']
    data.save()
    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    product_data=Productmodel.objects.all()
    # print(product_data)
    Context={
        'media_url': settings.MEDIA_URL,
        'admin_user':admin_info,
        'customer':product_data,
        'key':'Data Suceesfully Updated'
    }
    return render(request, 'productdata.html', Context)

def addproductdata(request):
    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    product_data=Productmodel.objects.all()
    # print(product_data)
    Context={
        'media_url': settings.MEDIA_URL,
        'admin_user':admin_info,
        'customer':product_data,
        'Productdataform':Productmodelform,
        'Addnewproduct':'add new Product',
        
    }
    return render(request, 'productdata.html', Context)

# =============== Ending Product data CRUD ===========================
#=================  USERDATA CRUD START=============================

def userdata(request):
    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    invoiceData = Invoicemodel.objects.all()
    Purchaseproductdata = Purchaseproduct.objects.all()
    Paymentdata = PaymentdataModel.objects.all()

    print(invoiceData)
    # customer_info=[]
    # for user in invoiceData:
        # cust_data=RegistrationModel.objects.get(id=user.Customer_id) 
        # customer_info.append(cust_data)

    # invoice_dict={
    #      "invoice_detail": invoiceData,
    #      "user_info": customer_info
    #     }

    Context={
        'media_url': settings.MEDIA_URL,
        'admin_user':admin_info,
        'all_invoice':invoiceData,
        'purchase_data':Purchaseproductdata,
        'Paymentdata':Paymentdata,
        # 'customer_data':customer_info
    }
    return render(request, 'userdata.html', Context)


# ---------------------- CRUD ------------------------------------

def deletpay(request, pk):
    try:
        data=Invoicemodel.objects.get(id=pk)
        data.delete()
        msg="Data Deleted Successfully"
    except:
        msg="Data does not exist"

    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    customer_data=RegistrationModel.objects.all()
    print(customer_data)
    invoiceData = Invoicemodel.objects.all()
    Purchaseproductdata = Purchaseproduct.objects.all()
    Paymentdata = PaymentdataModel.objects.all()
    Context={
        'media_url': settings.MEDIA_URL,
        'admin_user':admin_info,
        'customer':customer_data,
        'all_invoice':invoiceData,
        'purchase_data':Purchaseproductdata,
        'Paymentdata':Paymentdata,
        # 'key':msg
    }
    return render(request, 'userdata.html', Context)

# ---------- PaymentdataModel data deleting  -----------

def deletoder(request, pk):
    try:
        data=PaymentdataModel.objects.get(id=pk)
        data.delete()
        msg="Data Deleted Successfully"
    except:
        msg="Data does not exist"

    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    customer_data=RegistrationModel.objects.all()
    print(customer_data)
    invoiceData = Invoicemodel.objects.all()
    Purchaseproductdata = Purchaseproduct.objects.all()
    Paymentdata = PaymentdataModel.objects.all()
    Context={
        'media_url': settings.MEDIA_URL,
        'admin_user':admin_info,
        'customer':customer_data,
        'all_invoice':invoiceData,
        'purchase_data':Purchaseproductdata,
        'Paymentdata':Paymentdata,
        # 'key':msg
    }
    return render(request, 'userdata.html', Context)

# ------------ purchase Product deleting -----------
def deletpurch_prod(request, pk):
    try:
        data=Purchaseproduct.objects.get(id=pk)
        data.delete()
        msg="Data Deleted Successfully"
    except:
        msg="Data does not exist"

    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    customer_data=RegistrationModel.objects.all()
    print(customer_data)
    invoiceData = Invoicemodel.objects.all()
    Purchaseproductdata = Purchaseproduct.objects.all()
    Paymentdata = PaymentdataModel.objects.all()
    Context={
        'media_url': settings.MEDIA_URL,
        'admin_user':admin_info,
        'customer':customer_data,
        'all_invoice':invoiceData,
        'purchase_data':Purchaseproductdata,
        'Paymentdata':Paymentdata,
        # 'key':msg
    }
    return render(request, 'userdata.html', Context)


# ------------------------ invoice model (invoice view) -----------------------
import os

def invoiceview(request, pk):
    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    customer_data=RegistrationModel.objects.all()
    print(customer_data)
    invoiceData = Invoicemodel.objects.all()
    Purchaseproductdata = Purchaseproduct.objects.all()
    Paymentdata = PaymentdataModel.objects.all()
    
    try:
        pdf_file_path = os.path.join(settings.BASE_DIR,'invoice_pdf',f'{pk}.pdf')
        return FileResponse(open(pdf_file_path, 'rb'))
    except:
        Context={
            'media_url': settings.MEDIA_URL,
            'admin_user':admin_info,
            'customer':customer_data,
            'all_invoice':invoiceData,
            'purchase_data':Purchaseproductdata,
            'Paymentdata':Paymentdata,
            'key':'Data does not exist'
        }
        return render(request, 'userdata.html', Context)



# ===============================UserData CRUD END =============================

def result(request):
    Admin_id=request.session.get('Admin_id')
    admin_info=get_object_or_404(RegistrationModel, id=Admin_id)
    Context={
        'media_url': settings.MEDIA_URL,
        'admin_user':admin_info
    }
    return render(request, 'result.html', {'admin_user':admin_info})

# =================== Product adding functions =====================
def product_entry(request):
    Admin_id = request.session.get('Admin_id')
    admin_info = get_object_or_404(RegistrationModel, id=Admin_id)

    if request.method == "POST":
        print(request.POST)
        # try:
        MRP = int(request.POST.get('Prod_MRP'))
        print(MRP)
        # except (TypeError, ValueError):
        #     MRP = 0.0

        # offer = request.POST.get('Prod_Offer', "")
        offer = request.POST.get('Prod_Offer')
        print(offer)

        discount_off = ""
        special_char = ""
        discount = 0

        for char in offer:
            if char.isdigit():
                discount_off += char
            else:
                special_char += char

        print(discount_off)
        print(special_char)
        try:
            if discount_off:
                discount = MRP * int(discount_off) / 100
            elif offer.isdigit():
                discount=int(offer)
        except ValueError:
            discount = 0

        # tax = MRP * 12 / 100
        # Prod_gross_amount = MRP + tax

        print(request.FILES)
        serialno = request.POST.get('Serial_no')
        serialmodel = Productmodel.objects.filter(Serial_no=serialno)

        if serialmodel.exists():
            msg = "This data already exists."
            context = {
                'media_url': settings.MEDIA_URL,
                'admin_user': admin_info,
                'msg': msg,
            }
            return render(request, 'productform.html', context)
        else:
            form = Productmodelform(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.Discount = discount
                product.Prod_Price = MRP - discount
                product.save()

                msg = "Data submitted successfully"
                return redirect('productdata')
            else:
                msg = "There is some error, please try again"
                context = {
                    'media_url': settings.MEDIA_URL,
                    'admin_user': admin_info,
                    'msg': msg,
                    'form': form,
                }
                return render(request, 'productform.html', context)
    else:
        form = Productmodelform()
        context = {
            'media_url': settings.MEDIA_URL,
            'admin_user': admin_info,
            'form': form,
        }
        return render(request, 'productform.html', context)    
    
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
# ===============@@@@@$     Admin Panel        $@@@@===========================




#=================== User Dashboard login after Navition =============
