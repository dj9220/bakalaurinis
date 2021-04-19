from django.contrib import admin
from .models import Product, Supplier, Category, SubCategories, Matts, ProductInCheck, Check
# Register your models here.
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(SubCategories)
admin.site.register(Matts)
admin.site.register(ProductInCheck)
admin.site.register(Check)
