from django.shortcuts import render,redirect
from .models import Product,Review
from accounts.models import Cart,CartItems,Profile
from django.http import HttpResponseRedirect
# Create your views here.
def Home(requests):
      products=Product.objects.all()[0:5]
      trending=Product.objects.all()[0:5]
      whey=Product.objects.filter(category__category_name__contains='whey protein')
      print(products)
      return render(requests ,'Home.html',{'products':products,'trending':trending,'whey':whey})

def get_product(request,slug):
      product=Product.objects.get(slug=slug)
      review=Review.objects.filter(product=product)
      return render(request,'ProductDetails.html',{'product':product,'review':review})

def add_to_cart(request,slug):
      product=Product.objects.get(slug=slug)
      cart,_=Cart.objects.get_or_create(user=request.user,is_paid=False)
      cartitems=CartItems.objects.create(cart=cart,product=product)
      print(request.user.profile.get_cart_count())
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def get_cart(request):
      cart=Cart.objects.get(user=request.user,is_paid=False)
      cartitems=CartItems.objects.filter(cart=cart)
      return render(request,'Cart.html',{'cartitems':cartitems})


def delete_item(request,uuid):
      cart_item=CartItems.objects.get(uuid=uuid)
      cart_item.delete()
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
      


