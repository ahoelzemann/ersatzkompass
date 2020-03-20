from django.contrib import admin
from .models import Item, Unit, Category, Collection
# Register your models here.
admin.site.register(Item)
admin.site.register(Unit)
admin.site.register(Category)
admin.site.register(Collection)