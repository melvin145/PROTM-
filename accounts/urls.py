from django.urls import path
from .views import Login,Register,user_profile,Logout
urlpatterns=[
      path('/login',Login,name='login'),
      path('/signup',Register,name='signup'),
      path('/profile',user_profile,name='profile'),
      path('logout',Logout,name='logout')
]