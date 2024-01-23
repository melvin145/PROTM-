from django.urls import path
from .views import Home,get_product,add_to_cart,get_cart,delete_item

urlpatterns=[
      path('',Home,name='home'),
      path('<slug>/' ,get_product, name="get_product"),
      path('add_to_cart/<slug>',add_to_cart,name='add_cart'),
      path('cart',get_cart,name='cart'),
      path('delete/<uuid>',delete_item,name='delete_item')
]