from django.contrib import admin
from models import Category, Currency, CollectibleImage, Book
# Register your models here.


admin.site.register(Currency)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(CollectibleImage)

