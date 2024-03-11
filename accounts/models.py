from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from base.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Product
import random



class Address(BaseModel):
      name=models.CharField(max_length=100,null=True,blank=True)
      address=models.TextField(null=True,blank=True)
      pincode=models.CharField(max_length=100,null=True,blank=True)
      city=models.CharField(max_length=100,null=True,blank=True)
      number=models.CharField(max_length=100,null=True,blank=True)


class Profile(BaseModel):
      user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
      profile_image=models.ImageField(upload_to='profile',default='51f6fb256629fc755b8870c801092942.png')
      address=models.OneToOneField(Address,on_delete=models.SET_NULL,null=True,blank=True)

      def get_cart_count(self):
            return CartItems.objects.filter(cart__is_paid=False,cart__user=self.user).count()


class Cart(BaseModel):
      user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='cart')
      is_paid=models.BooleanField(default=False)

      def get_subtotal(self):
            cart_items = self.cart_item.all()
            total_amount=0
            for cart_item in cart_items:
                  total_amount+=cart_item.product.updated_price;
            return total_amount
      
      def get_cart_total(self):
            subtotal_amount=self.get_subtotal()
            delivery_charge=500            
            subtotal_amount+=delivery_charge
            return subtotal_amount

      def get_all_items(self):
            return self.cart_item.all()
            

      

      def __str__(self):
            return self.user.first_name +'\tCart'
      
class CartItems(BaseModel):
      cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart_item')
      product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product')



@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
      try:
            if created:
                  Profile.objects.create(user=instance)
      except Exception as e:
            print(e)

class Order(BaseModel):
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      order_id=models.CharField(max_length=100,null=True,blank=True)
      order_items=models.OneToOneField(Cart,on_delete=models.CASCADE,blank=True,null=True)
      order_amount=models.IntegerField(null=True,blank=True)
      status_choices=(
            ('PENDING','NOT PACKED'),
            ('PACKED','PACKED'),
            ('SHIPPED', 'Shipped'),
             ('DELIVERED', 'Delivered'),
            )
      status=models.CharField(max_length=20,choices=status_choices,default='1')
      payment_status_choices = (
        (1, 'SUCCESS'),
        (2, 'FAILURE' ),
        (3, 'PENDING'),
      )
