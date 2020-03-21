from django.contrib import admin
from .models import Item, Category, Subcategory, Substitution, Comment
# Register your models here.
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Substitution)
admin.site.register(Comment)