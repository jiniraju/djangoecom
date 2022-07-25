from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import *
from django.contrib.auth import authenticate,login,logout
import os
from App1.models import adduser_model,catogery_model,add_product_model,add_cart


# Create your views here.

# to load home
def load_home(request):
    cat=catogery_model.objects.all()
    context={'cat':cat}
    return render(request,'home.html',context)

# to load login
def load_login(request):
    return render(request,'signin.html')

# to load signup
def load_signup(request):
    return render(request,'signup.html')

# to sign up
def register(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['mail']
        gender=request.POST['gen']
        uname=request.POST['uname']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if request.FILES.get('file') is not None:
            photo = request.FILES['file']
            print("photo added")
        else :
            photo = '/static/images/no-photo-icon-loading-images-.jpg'
            print("default photo added")
        if password == cpassword:
            if User.objects.filter(username=uname).exists():
                return redirect('load_signup')
                print("username already taken")
            elif User.objects.filter(email=email).exists():
                return redirect('load_signup')
                print("mail already taken")
            else:
                user=User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=uname,
                    email=email,
                    password=password)
                user.save()        
                u=User.objects.get(id=user.id)
                adduser=adduser_model(gender=gender,image=photo,user=u)
                adduser.save()
                print("create successfully")
        else:
            return redirect('load_signup')
            print("pasword didnt match")
        return redirect('load_login')
    else:
        return redirect('load_signup')

# to login
def user_login(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        password=request.POST['password']
        user=auth.authenticate(username=uname,password=password)
        if user is not None:
            if user.is_staff:
                return redirect('load_admin_home')
            else:
                login(request,user)
                auth.login(request,user)
                return redirect('load_home')
        else:
            return redirect('load_login')
    else:
        return redirect('load_login')

# to logout
def user_logout(request):
    auth.logout(request)
    return redirect('load_home')

# to show user details
def userdetails(request):
    user_detail = adduser_model.objects.all()
    return render(request,'showuser.html',{'user_detail':user_detail})

# to show user personal profile
def userprofileview(request):
    user_detail = adduser_model.objects.get(user=request.user)
    return render(request,'userprofile.html',{'user_detail':user_detail})

# to load_add_catogery
def load_admin_home(request):
    return render(request,'adminhome.html')

# to load_add_catogery
def load_add_catogery(request):
    return render(request,'addcatogery.html')

def add_catogery(request):
    if request.method == "POST":
        name=request.POST['cname']
        data = catogery_model(name=name)
        data.save()
    return redirect('load_add_catogery')

# to show catogery
def catogery_Details(request):
        cat=catogery_model.objects.all()
        return render(request,'showcatogery.html',{'cat':cat})

# to load add product
def load_add_product(request):
    cat=catogery_model.objects.all()
    return render(request,'addproduct.html',{'cat':cat})

# to add product
def add_product(request):
    if request.method == "POST":
        photo = request.FILES['file']
        name=request.POST['pname']
        qnt=request.POST['qnt']
        price=request.POST['price']
        availability=request.POST['avail']
        select=request.POST['select']
        cat=catogery_model.objects.get(id=select)
        data = add_product_model(image=photo,name=name,price=price,quantity=qnt,availability=availability,catogery=cat)
        data.save()
        return redirect('load_add_product')

# to delete user 
def del_user(request,pk):
    user = adduser_model.objects.get(id=pk)
    user.delete()
    return redirect('userdetails')

# to show product details
def ProductDetails(request):
    product = add_product_model.objects.all()
    return render(request,'viewproduct.html',{'product':product})

def UserProductDetails(request):
    product = add_product_model.objects.all()
    return render(request,'userproductview.html',{'product':product})

# to delete user 
def del_product(request,pk):
    product = add_product_model.objects.get(id=pk)
    product.delete()
    return redirect('ProductDetails')

# to load edit user profile
def load_edit(request):
    user=adduser_model.objects.get(user=request.user)
    context={'user':user}
    return render(request,'edit.html',context)

# to edit user profile
def edit_user(request):
    if request.method == 'POST':
        member=adduser_model.objects.get(user=request.user)
        member.user.first_name=request.POST['fname']
        member.user.last_name=request.POST['lname']
        member.gender=request.POST['gen']
        # member.image=request.FILES['file']
        # if request .FILES.get('file') is not None:
        #     if not member.image == "/static/images/no-photo-icon-loading-images-.jpg":
        #         os.remove(member.image.path)
        #         member.image="/static/images/no-photo-icon-loading-images-.jpg"
        member.save()
        member.user.save()
        return redirect('userprofileview')

# to load cart page
def load_cart(request):
    products=add_cart.objects.filter(user=request.user)
    context={'products':products}
    return render(request,'cart.html',context)


# to add to cart product 
def add_caart(request,pk):
    product = add_product_model.objects.get(id=pk)
    # user = adduser_model.objects.get(user=request.user)
    data = add_cart(product=product,user=request.user)
    data.save()
    return redirect('UserProductDetails')

# to delete items in cart 
def del_item_cart(request,pk):
    product = add_cart.objects.get(id=pk)
    product.delete()
    return redirect('load_cart')

# to edit product details
# def edit_product(request):
#     if request.method == 'POST':
#         prt=add_product_model.objects.get(user=request.user)
#         prt.user.first_name=request.POST['fname']
#         prt.user.last_name=request.POST['lname']
#         prt.gender=request.POST['gen']
#         # prt.image=request.FILES['file']
#         # if request .FILES.get('file') is not None:
#         #     if not prt.image == "/static/images/":
#         #         os.remove(prt.image.path)
#         #         prt.image="/static/images/no-photo-icon-loading-images-.jpg"
#         prt.save()
#         prt.user.save()
#         return redirect('userprofileview')



def edit_product_details(request,pk):
    if request.method=='POST':
        products = add_product_model.objects.get(id=pk)
        products.name = request.POST['pname']
        products.price = request.POST['price']
        products.quantity = request.POST['qnt']
        products.availability = request.POST['avail']
        # products.image=request.FILES['file']
        products.save()
        return redirect('ProductDetails')
    products=add_product_model.objects.get(id=pk)
    return render(request,'productedit.html',{'products':products})
    
