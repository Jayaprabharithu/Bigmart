from django.shortcuts import render,redirect
from Backend.models import Category_db,product_db
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
import datetime
from webapp.models import contactdb


# Create your views here.
def index_page(req):
    x=datetime.datetime.now()
    return render(req,"index.html",{'d':x})

def add_category(req):
    return render(req,"add_category.html")

def save_category(req):
    if req.method=="POST":
        a=req.POST.get("name")
        b=req.POST.get("dis")
        c=req.FILES['image']
        obj=Category_db(Category_Name=a,Description=b,Category_image=c)
        obj.save()
        messages.success(req,"Successfully Saved")
        return redirect(add_category)

def view_category(req):
    data=Category_db.objects.all()
    return render(req,"display_category.html",{"data":data})

def edit_category(req,cid):
    data=Category_db.objects.get(id=cid)
    return render(req,"edit_category.html",{"data":data})
def update_category(req,cid):
    if req.method=="POST":
        a=req.POST.get("name")
        b=req.POST.get("dis")
        try:
            img=req.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=Category_db.objects.get(id=cid).Category_image
        Category_db.objects.filter(id=cid).update(Category_Name=a,Description=b,Category_image=file)
        return redirect(view_category)

def delete_category(req,cid):
    Category_db.objects.filter(id=cid).delete()
    messages.error(req,"Delete successfully")
    return redirect(view_category)
def admin_login(req):
    return render(req,"login_admin.html")
def login_page(request):
    if request.method=="POST":
        un=request.POST.get('Name')
        pwd=request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd

                return redirect(index_page)
            else:
                messages.warning(request,"Invalid User name or Password")
                return redirect(admin_login)
        else:
            messages.warning(request,"User Not Found")
            return redirect(admin_login)


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.error(request,"Log Out")
    return redirect(admin_login)

def product_add(req):
    cat = Category_db.objects.all()
    return render(req,"addproduct.html",{'cat':cat})

def save_product(req):
    if req.method=="POST":
        a=req.POST.get("cat_name")
        b=req.POST.get("name")
        c=req.POST.get("price")
        d=req.POST.get("dis")
        e=req.FILES['image']
        obj=product_db(Category=a,Product_name=b,Price=c,pro_Description=d,pro_image=e)
        obj.save()
        messages.success(req, "Successfully Saved")
        return redirect(product_add)

def view_product(req):
    data=product_db.objects.all()
    return render(req,"display_product.html",{'data':data})

def edit_product(req,pid):
    data=product_db.objects.get(id=pid)
    cat=Category_db.objects.all()
    return render(req,"edit_product.html",{'data':data,'cat':cat})

def update_product(req,pid):
    if req.method=="POST":
        a=req.POST.get("cat_name")
        b = req.POST.get("name")
        c = req.POST.get("price")
        d = req.POST.get("dis")
        try:
            img=req.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=product_db.objects.get(id=pid).pro_image
        product_db.objects.filter(id=pid).update(Category=a,Product_name=b,Price=c,pro_Description=d,pro_image=file)
        return redirect(view_product)

def delete_product(req,pid):
    product_db.objects.filter(id=pid).delete()
    messages.error(req,"Successfully Deleted")
    return redirect(view_product)

def contact_details(req):
    data=contactdb.objects.all()
    return render(req,"contact_data.html",{'data':data})