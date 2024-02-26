from django.shortcuts import render,redirect
from .models import Product,Review
from accounts.models import Cart,CartItems,Profile,Order,Address
from .models import Category
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.db.models import Q
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def Home(requests):
      products=Product.objects.all()[0:5]
      trending=Product.objects.all()[0:5]
      whey=Product.objects.filter(category__category_name__contains='whey protein')
      categories=Category.objects.all()
      print(products)
      return render(requests ,'Home.html',{'products':products,'trending':trending,'whey':whey,'categories':categories})

def get_product(request,slug):
      product=Product.objects.get(slug=slug)
      if request.method=='POST':
            review=request.POST.get('review')
            if review!=" ":
                  new_review=Review.objects.create(product=product,user=request.user,content=review)
                  new_review.save()
                  return HttpResponseRedirect(request.path_info)
            
      review=Review.objects.filter(product=product).order_by("-created_at")
      print(request.user)
      return render(request,'ProductDetails.html',{'product':product,'review':review})


def add_to_cart(request,slug):
      product=Product.objects.get(slug=slug)
      cart,_=Cart.objects.get_or_create(user=request.user,is_paid=False)
      try:
            cartitems=CartItems.objects.get(cart=cart,product=product)
            if cartitems:
                  product.quantity+=1;
                  product.save()
      except:
            cartitems=CartItems.objects.create(cart=cart,product=product)
      print(request.user.profile.get_cart_count())
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_from_cart(request,slug):

      product=Product.objects.get(slug=slug)

      cart=Cart.objects.get(user=request.user,is_paid=False)
      try:
            cartitem=CartItems.objects.get(cart=cart,product=product)

            if cartitem and product.quantity>1:
                  product.quantity-=1;
                  product.save()
            else:
                  print('deleted')
                  delete_item(request,cartitem.uuid)
      except:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

      print(request.user.profile.get_cart_count())
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def get_cart(request):
      try:
            cart=Cart.objects.get(user=request.user,is_paid=False)
            
            cartitems=CartItems.objects.filter(cart=cart)
            subtotal_amount=cart.get_subtotal()
            total_amount=cart.get_cart_total()
            return render(request,'Cart.html',{'cartitems':cartitems,"total":total_amount,'subtotal':subtotal_amount,'cart':cart})
      except:
            print('error')
      return render(request,'Cart.html')


def delete_item(request,uuid):
      cart_item=CartItems.objects.get(uuid=uuid)
      cart_item.delete()
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def Categorie(request,slug):
      products=Product.objects.filter(category__slug__contains=slug)
      return render(request,'products.html',{'products':products})


def list_products(request):
      category=request.GET.get('category')
      ordering=request.GET.get('ordering')
      search=request.GET.get('search')
      if search:
            products=Product.objects.filter(Q(product_name__icontains=search)| Q(category__category_name__icontains=search))
      else:
            products=Product.objects.all()
      if category:
            products=products.filter(category__category_name=category)
      if ordering:
            products=products.order_by(ordering)
      category=Category.objects.all()
      return render(request,"products.html",{'products':products,'category':category})

@csrf_exempt
def payment(request,uuid):

      address=Profile.objects.get(user=request.user).address
      
      cart=Cart.objects.get(uuid=uuid)
      client=razorpay.Client(auth=(settings.RAZORPAY_ID,settings.RAZORPAY_SECRET))
      payment=client.order.create({'amount':cart.get_cart_total()*100,'currency':'INR'})

      context={
            'order_amount':cart.get_cart_total(),
            'payment':payment,
            'address':address
            }
      
      order,_=Order.objects.get_or_create(user=request.user,order_items=cart,order_amount=cart.get_cart_total(),)
      order.order_id=payment['id']
      order.save()
            

      return render(request,'Payment.html',context)

@csrf_exempt
def payment_success(request):
      userprofile=Profile.objects.get(user=request.user)
      if request.method=='POST' and userprofile.address==None:
            name=request.POST.get('name')
            address=request.POST.get('address')
            city=request.POST.get('city')
            pincode=request.POST.get('pincode')
            number=request.POST.get('phonenumber')

            address_obj=Address.objects.create(name=name,address=address,city=city,pincode=pincode,number=number)
            address_obj.save()


            userprofile.address=address_obj
            userprofile.save()
      else:
            address=userprofile.address
      
      order_id=request.GET.get('order_id')
      order=Order.objects.get(order_id=order_id)
      print(order.order_items)
      order.order_items.is_paid=True
      order.order_items.save()
      order.save()
      return render(request,'success.html')
      


