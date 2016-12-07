import os
from django.db import models
from Collector import settings


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


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, null=True)
    isbn = models.CharField("ISBN", max_length=20, null=True)
    description = models.CharField(max_length=1000, null=True)
    date_aquired = models.DateTimeField('date aquired', null=True, blank=True)
    price = models.IntegerField(default=0)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail = models.FileField(upload_to='book_images/', blank=True, null=True)
    published_date = models.DateTimeField('Published date', null=True, blank=True)

    def __unicode__(self):
        return self.name

    @property
    def image_url(self):
        if self.thumbnail and hasattr(self.thumbnail, 'url'):
            return self.thumbnail.url


class CollectibleImage(models.Model):
    image = models.FileField(upload_to='book_images/')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
