from django.db import models


# Create your models here.


class Customer(models.Model):
	first_name=models.CharField(max_length=25,blank=True)
	last_name=models.CharField(max_length=25,blank=True)
	email=models.EmailField(max_length=70,blank=True)
	contact_no=models.IntegerField()
	dob= models.DateTimeField(blank=True)
	history=models.ManyToManyField('Product', related_name='customers', blank=True)

	def __str__(self):
		return self.first_name + " " + self.last_name


class Product(models.Model):
	name=models.CharField(max_length=100,blank=True)
	brand=models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='products', blank=True)
	category=models.ManyToManyField('Category', related_name='products', blank=True)
	price=models.IntegerField()
	dicount=models.FloatField()
	rating=models.IntegerField()
	delivery=models.IntegerField()
	history=models.ManyToManyField('Customer',related_name='products', blank=True)

	def __str__(self):
		return self.name

class Brand(models.Model):
	name=models.CharField(max_length=100,blank=True)
	categories_active=models.ManyToManyField('Category', related_name='brands')
	rating=models.FloatField()	

	def __str__(self):
		return self.name

class Category(models.Model):
	name=models.CharField(max_length=25)

	def __str__(self):
		return self.name




