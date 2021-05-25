from django.db import models

# Create your models here.

class Person(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  number = models.IntegerField(null=True)

  def __str__(self):
    return self.first_name + "" + self.last_name

class Plug(models.Model):
  first_name = models.CharField(max_length=30)
  number = models.IntegerField(null=True)

  def __str__(self):
    return self.first_name 

class Product(models.Model):
  product = models.CharField(max_length=30)
  inventory = models.CharField(max_length=30)

  def __str__(self):
    return self.product + "" + self.inventory
