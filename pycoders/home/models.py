from django.db import models

from django.contrib.auth.models import User

import datetime


# Create your models here.


class Customer(models.Model):
	first_name=models.CharField(max_length=25,blank=True)
	last_name=models.CharField(max_length=25,blank=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='static/uploads/avatar', null=True, blank=True)
	email=models.EmailField(max_length=70,blank=True)
	contact_no=models.IntegerField()
	address=models.CharField(max_length=100, blank=True)
	city=models.CharField(max_length=100, blank=True)
	dob= models.DateTimeField(blank=True)
	history=models.ManyToManyField('Product', related_name='customers', blank=True)
	friends=models.ManyToManyField('Customer', related_name='_friends', blank=True)
	wishlist=models.ManyToManyField('Product', related_name='customers_wishlist', blank=True)
	ineterests = models.ManyToManyField('Category', related_name='customers_interests', blank=True)

	def __str__(self):
		return self.first_name + " " + self.last_name

# class SearchTerm(models.Model):
# 	name = models.CharField(max_length=100,blank=True, null=True)

# 	def __str__(self):
# 		return self.name

class Product(models.Model):
	name=models.CharField(max_length=100,blank=True)
	brand=models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='products', blank=True)
	image = models.ImageField(upload_to='static/uploads/product', null=True, blank=True)
	image1 = models.ImageField(upload_to='static/uploads/product', null=True, blank=True)
	image2 = models.ImageField(upload_to='static/uploads/product', null=True, blank=True)
	category=models.ManyToManyField('Category', related_name='products', blank=True)
	description=models.TextField(blank=False, null=False)
	price=models.IntegerField()
	dicount=models.FloatField()
	rating=models.IntegerField()
	review = models.ManyToManyField('Review', related_name='product_review', blank=True, null=True)
	delivery=models.IntegerField()
	search = models.CharField(max_length=200, blank=True, null=True)
	history=models.ManyToManyField('Customer',related_name='products', blank=True) #To store the users who viewed th product
	

	def __str__(self):
		return self.name

class Brand(models.Model):
	name=models.CharField(max_length=100,blank=True)
	image = models.ImageField(upload_to='static/uploads/brand', null=True, blank=True)
	categories_active=models.ManyToManyField('Category', related_name='brands')
	customers=models.ManyToManyField('Customer', related_name='brands')
	rating=models.FloatField()	

	def __str__(self):
		return self.name

class Category(models.Model):
	name=models.CharField(max_length=25)

	def __str__(self):
		return self.name

class Store(models.Model):
	name=models.CharField(max_length=50)
	location=models.CharField(max_length=50)
	email=models.EmailField()
	contact_no=models.IntegerField()
	brand=models.ManyToManyField('Brand', related_name='stores')
	customers=models.ManyToManyField('Customer', related_name='stores')

	def __str__(self):
		return self.name



class TimeStamp(models.Model):
	date=models.DateField(default=datetime.datetime.now())
	customer=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='date', blank=True)
	product=models.ForeignKey('Product', on_delete=models.CASCADE, related_name='date', blank=True)


class Review(models.Model):
	review = models.TextField()

	def __str__(self):
		return self.review