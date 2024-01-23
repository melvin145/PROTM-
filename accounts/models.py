from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from base.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Product

class Profile(BaseModel):
      user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
      profile_image=models.ImageField(upload_to='profile',default='51f6fb256629fc755b8870c801092942.png')

      def get_cart_count(self):
            return CartItems.objects.filter(cart__is_paid=False,cart__user=self.user).count()


class Cart(BaseModel):
      user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='cart')
      is_paid=models.BooleanField(default=False)

      def __str__(self):
            return self.user.first_name +'\tCart'
      
class CartItems(BaseModel):
      cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart')
      product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product')

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
      try:
            if created:
                  Profile.objects.create(user=instance)
      except Exception as e:
            print(e)
