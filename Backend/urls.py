from django.urls import path
from Backend import views
urlpatterns=[
    path('index_page/',views.index_page,name="index_page"),
    path('add_category/',views.add_category,name="add_category"),
    path('save_category/',views.save_category,name="save_category"),
    path('view_category/',views.view_category,name="view_category"),
    path('edit_category/<int:cid>/',views.edit_category,name="edit_category"),
    path('update_category/<int:cid>/',views.update_category,name="update_category"),
    path('delete_category/<int:cid>/',views.delete_category,name="delete_category"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('login_page/',views.login_page,name="login_page"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),


    path('product_add/',views.product_add,name="product_add"),
    path('save_product/',views.save_product,name="save_product"),
    path('view_product/',views.view_product,name="view_product"),
    path('edit_product/<int:pid>/',views.edit_product,name="edit_product"),
    path('update_product/<int:pid>/',views.update_product,name="update_product"),
    path('delete_product/<int:pid>/',views.delete_product,name="delete_product"),


    path('contact_details/',views.contact_details,name="contact_details"),


]
