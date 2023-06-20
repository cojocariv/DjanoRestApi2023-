from django.contrib import admin
from .models import Product
from .models import Car

admin.site.register(Product)
admin.site.register(Car)