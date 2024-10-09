from django.shortcuts import render,redirect
from Backend.models import product_db,Category_db
from webapp.models import contactdb,signup_db,cartdb,checkoutdb
from django.contrib import messages
import razorpay
# Create your views here.
def home_page(req):
    cat=Category_db.objects.all()
    return render(req,"home_page.html",{'cat':cat})
def about_page(req):
    cat = Category_db.objects.all()
    return render(req,"about_page.html",{'cat':cat})
def contact_page(req):
    cat = Category_db.objects.all()
    return render(req,"contact_page.html",{'cat':cat})

def save_contact(req):
    if req.method=="POST":
      a =req.POST.get("name")
      b=req.POST.get("email")
      c=req.POST.get("subject")
      d=req.POST.get("message")
      e=req.POST.get("phone")
      obj=contactdb(Name=a,Email=b,Subject=c,Message=d,Mobile=e)
      obj.save()
      return redirect(contact_page)

def webproduct_page(req):
    pro=product_db.objects.all()
    cat = Category_db.objects.all()
    return render(req,"web_product.html",{'pro':pro,'cat':cat})

def filterd_product(req,categoryname):
    data=product_db.objects.filter(Category=categoryname)
    # pro=product_db.objects.get(Product_name=categoryname)
    return render(req,"product_filterd.html",{'data':data})
def single_propage(req,proid):
    data=product_db.objects.get(id=proid)
    return render(req,"single_product.html",{'data':data})

def register_page(req):
    return render(req,"register.html")
def save_signuppage(req):
    if req.method=="POST":
      a =req.POST.get("suser")
      b=req.POST.get("semail")
      c=req.POST.get("spass")
      c1=req.POST.get("s2pass")
      d=req.FILES["simage"]
      obj=signup_db(Username=a,Email=b,Password=c,Confirm_Password=c1,Profileimage=d)
      if signup_db.objects.filter(Username=a).exists():
          messages.warning(req,"user already exists...!")
      elif signup_db.objects.filter(Email=b).exists():
          messages.warning(req, "email already exists...!")
      else:
          obj.save()
          messages.success(req, "save successfully..!")
      return redirect(register_page)

def userlogin(request):
    if request.method=="POST":
        un = request.POST.get("uname")
        pwd = request.POST.get("pass")
        if signup_db.objects.filter(Username=un, Password=pwd).exists():
            request.session['Username']=un
            request.session['Password']=pwd
            return redirect(home_page)
        else:
            return redirect(register_page)

    else:
        return redirect(register_page)
def userlogout(req):
    del req.session['Username']
    del req.session['Password']
    return redirect(home_page)

def save_cart(req):
    if req.method=="POST":
      un =req.POST.get("username")
      pn=req.POST.get("proname")
      qua=req.POST.get("qun")
      tot=req.POST.get("total")
      obj=cartdb(Username=un,Productname=pn,Quantity=qua,Totalprice=tot)
      obj.save()
      messages.success(req,"Added to cart")
      return redirect(home_page)

def cart_page(req):
    data=cartdb.objects.filter(Username=req.session['Username'])
    total_price=0
    shipping_charge=0
    Subtotal=0
    for i in data:
        total_price=total_price+i.Totalprice
        if total_price>500:
            shipping_charge=50
        else:
            shipping_charge=100
    Subtotal=total_price+shipping_charge

    return render(req,"cart.html",{'data':data,'total_price':total_price,'shipping_charge':shipping_charge,'Subtotal':Subtotal})

def login_page(req):
    return render(req,"login_page.html")
def checkout_page(request):
    products = cartdb.objects.filter(Username=request.session['Username'])
    total_price = 0
    shipping_charge = 0
    Subtotal = 0
    for i in products:
        total_price = total_price + i.Totalprice
        if total_price > 500:
            shipping_charge = 50
        else:
            shipping_charge = 100
    Subtotal = total_price + shipping_charge
    return render(request,"checkout.html",{'products':products,'total_price':total_price,'shipping_charge':shipping_charge,'Subtotal':Subtotal})
def payment_page(request):
    customer=checkoutdb.objects.order_by('-id').first()
    pay=customer.Total
    amount=int(pay*100)
    pay_str=str(amount)
    for i in pay_str:
        print(i)
    if request.method=="POST":
        order_currency='INR'
        client=razorpay.Client(auth=('rzp_test_86iQru7GwgZ04r','rOfUvoSeP6JFplcD80bzJOFk'))
        payment=client.order.create({'amount':amount,'currency':order_currency,'payment_capture':'1'})

    return render(request,"payment.html",{'customer':customer,'pay_str':pay_str})
def save_checkout(request):
    if request.method=="POST":
      un =request.POST.get("user")
      em=request.POST.get("email")
      add=request.POST.get("address")
      ph=request.POST.get("phone")
      Tot=request.POST.get("total")
      mess=request.POST.get("bill")
      obj = checkoutdb(Username=un, Email=em, Address=add, Phone=ph,Total=Tot,saysomething=mess)
      obj.save()
      return redirect(payment_page)
