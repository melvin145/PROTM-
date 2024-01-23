from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
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
      description=models.TextField()
      weight=models.IntegerField()
      serve_size=models.IntegerField()
      no_of_servings=models.IntegerField()

      def save(self,*args,**kwargs):
            self.slug=slugify(self.product_name)
            super(Product,self).save(*args,**kwargs)
      
      def __str__(self):
            return self.product_name
      
class Review(BaseModel):
      product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
      user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
      content=models.TextField()

      def __str__(self):
            return self.user.username + '\t review'
