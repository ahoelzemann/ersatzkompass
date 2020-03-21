from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.name)

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "%s" % (self.name)

class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "%s" % (self.name)

    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'pk': self.pk})

class Substitution(models.Model):
    item_missing = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    items_needed = models.ManyToManyField(Item, related_name = 'items_needed')
    description_of_creation = models.TextField(blank=True)

class Comment(models.Model):
    name = models.CharField(max_length=100, blank=False)
    text = models.TextField(blank=True)
    substitution = models.ForeignKey(Substitution, related_name ='comments', on_delete=models.DO_NOTHING)

    def __str__(self):
        return "%s: %s" % (self.name, self.text)