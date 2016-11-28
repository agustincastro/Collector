from django.contrib import admin
from models import Category, Currency, CollectibleImage, Book, Author
# Register your models here.


admin.site.register(Currency)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(CollectibleImage)
admin.site.register(Author)