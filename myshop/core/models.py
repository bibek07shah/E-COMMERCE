from django.db import models
from accounts.models import CustomUserModel
# Create your models here.
class OfferProduct(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    image=models.ImageField(upload_to='offer_products')


class Category(models.Model): #men,electronic,kid,
    title=models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
class Brand(models.Model): #men,electronic,kid,
    title=models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
class SubCategory(models.Model): #mobile
    title=models.CharField(max_length=200)#mobile
    category=models.ForeignKey(Category, on_delete=models.CASCADE) #electronic
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    name=models.CharField(max_length=200) #samsung s21
    category=models.ForeignKey(Category, on_delete=models.CASCADE) #electronic
    subcategory=models.ForeignKey(SubCategory, on_delete=models.CASCADE)#mobile
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)#mobile
    desc=models.TextField()
    image=models.ImageField(upload_to="product_image")
    image2=models.ImageField(upload_to="product_image")
    image3=models.ImageField(upload_to="product_image")
    mark_price=models.DecimalField(max_digits=8,decimal_places=2) #100
    discount_percent=models.DecimalField(max_digits=4,decimal_places=2)#10
    price=models.DecimalField(max_digits=8,decimal_places=2,editable=False)#90
    created_date=models.DateTimeField(auto_now=True)
    
    # -->100*(1-10/100) -->100*(1-0.1) -->100 * 0.9 -->90
    
    
    
    def save(self,*args, **kwargs):
        self.price=self.mark_price*(1-self.discount_percent/100)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Order(models.Model):
    product=models.CharField(max_length=200)
    user=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)
    phone=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    quantity=models.PositiveSmallIntegerField()
    price=models.CharField(max_length=20)
    total=models.CharField(max_length=20)
    image=models.ImageField(upload_to='Order_Product')
    is_pay=models.BooleanField(default=False)
    order_date=models.DateTimeField(auto_now=True)