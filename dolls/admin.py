from django.contrib import admin

# Register your models here.
from .models import Person, Product,Plug

admin.site.register(Person)
admin.site.register(Product)
admin.site.register(Plug)
