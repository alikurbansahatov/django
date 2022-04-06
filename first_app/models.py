from pydoc import describe
from django.db import models

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class Category(models.Model):
    category_id = models.IntegerField(unique=True)
    category_name = models.CharField(max_length=264, unique=True)

class Brand(models.Model):
    brand_id = models.IntegerField(unique=True)
    brand_name = models.CharField(max_length=264, unique=True)
    brand_rating = models.IntegerField()

class Product(models.Model):
    product_id = models.IntegerField(unique=True)
    product_name = models.CharField(max_length=264)
    product_description = models.CharField(max_length=264)
    product_price = models.FloatField()
    product_brand = models.ForeignKey(Brand, on_delete=models.SET_NULL)
    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL)

# Create your models here.
