from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Profile,Order
from products.views import Home
# Create your views here.
def Login(request):
      if request.method=='POST':

            email=request.POST.get('email')
            password=request.POST.get('password')
            user_obj=User.objects.filter(username=email).first()
            print(email,password)
            if not user_obj:
                  messages.warning(request,'Account doesnt exist')
            authenticate(email=email,password=password)
            print(user_obj)

            if user_obj:
                  print('logined')
                  login(request,user_obj)
                  return redirect('/')
                  
      return render(request,'accounts/login.html')

def Register(request):
      if request.method=='POST':
            firstname=request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            email=request.POST.get('email')
            password=request.POST.get('password')
            user_obj=User.objects.filter(username=email)

            if user_obj.exists():
                  messages.warning(request,'email is already taken')
                  return HttpResponseRedirect(request.path_info)
            
            user_obj=User.objects.create_user(email=email,username=email)
            user_obj.set_password(password)
            user_obj.first_name=firstname
            user_obj.last_name=lastname
            user_obj.save()

            return redirect(Login)
                  
            
      return render(request,'accounts/signup.html')

def user_profile(request):
      profile=Profile.objects.get(user=request.user)
      orders=Order.objects.filter(user=request.user)
      context={
            'profile':profile,
            'orders':orders
      }
      return render(request,'profile.html',context)

def Logout(request):
      logout(request)
      return redirect(Login)

