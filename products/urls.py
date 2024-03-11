from django.urls import path
from .views import Home,get_product,add_to_cart,get_cart,delete_item,Categorie,list_products,remove_from_cart,payment_success,payment,allorders,order_details


urlpatterns=[
      path('',Home,name='home'),
      path('getproduct/<slug>/' ,get_product, name="get_product"),
      path('add_to_cart/<slug>',add_to_cart,name='add_cart'),
      path('remove_from_cart/<slug>',remove_from_cart,name='remove_cart'),
      path('cart',get_cart,name='cart'),
      path('delete/<uuid>',delete_item,name='delete_item'),
      path('categories/<slug>',Categorie,name='categorie'),
      path('listproducts/',list_products,name='list_products'),
      path('payment/<str:uuid>',payment,name='payment'),
      path('payment/success/',payment_success,name='success'),
      path('allorder',allorders,name='allorder'),
      path('order_details/<str:id>',order_details,name='order_details')
]