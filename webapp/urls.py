from django.urls import path
from webapp import views
urlpatterns=[
    path('',views.home_page,name="home"),
    path('about/',views.about_page,name="about"),
    path('contact/',views.contact_page,name="contact"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('product/',views.webproduct_page,name="product"),
    path('filterd_product/<categoryname>/',views.filterd_product,name="filterd_product"),

    path('single_propage/<int:proid>/',views.single_propage,name="single_propage"),

    path('register_page/',views.register_page,name="register_page"),
    path('save_signuppage/',views.save_signuppage,name="save_signuppage"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('login_page/',views.login_page,name="login_page"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('checkout_page/',views.checkout_page,name="checkout_page"),
    path('payment_page/',views.payment_page,name="payment_page"),
    path('save_checkout/',views.save_checkout,name="save_checkout"),



]