from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.

class Category(BaseModel):
      category_name=models.CharField(max_length=100)
      slug=models.SlugField(unique=True,null=True,blank=True)
      category_image=models.ImageField(upload_to='categories')
      
      def __str__(self):
            return self.category_name
      
      def save(self,*args,**kwargs):
            self.slug=slugify(self.category_name)
            super(Category,self).save(*args,**kwargs)

class Product(BaseModel):
      product_name=models.CharField(max_length=100)
      product_image=models.ImageField(upload_to='products',null=True)
      slug=models.SlugField(unique=True,null=True,blank=True)
      category=models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products')
      price=models.IntegerField()
      updated_price=models.IntegerField(null=True,blank=True)
      description=models.TextField()
      weight=models.IntegerField()
      serve_size=models.IntegerField()
      no_of_servings=models.IntegerField()
      quantity=models.PositiveIntegerField(default=1,validators=[MinValueValidator(1)])
      flavour=models.CharField(max_length=100,blank=True,null=True)
      expiry=models.CharField(max_length=100,null=True,blank=True)
      brand=models.CharField(max_length=100,null=True,blank=True)
      when_to_use=models.TextField(null=True,blank=True)
      how_to_use=models.TextField(null=True,blank=True)

      def save(self,*args,**kwargs):
            self.slug=slugify(self.product_name)
            self.updated_price=self.price * self.quantity
            super(Product,self).save(*args,**kwargs)

            ###
            # price=10 qnt=2
            #price=price(10)*2
            #price=20 qnt=4
            #updated_price=price(10)*4
            #updated_price=40
            # updated_price=price(10)*30
            # updated_price =price()
      
      def __str__(self):
            return self.product_name
      
class Review(BaseModel):
      product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
      user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
      description=models.TextField(null=True,blank=True)

      def __str__(self):
            return self.user.username + '\t review'
      

