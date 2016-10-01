from __future__ import unicode_literals
from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=5)
    def __unicode__(self):
       return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True)
    def __unicode__(self):
       return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=1000, null=True)
    date_aquired = models.DateTimeField('date aquired', null=True, blank=True)
    price = models.IntegerField(default=0)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail = models.FileField(upload_to='book_images/', default='settings.STATIC_URL/images/no_image.png')

    def __unicode__(self):
       return self.name


class CollectibleImage(models.Model):
    image = models.FileField(upload_to='book_images/')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)