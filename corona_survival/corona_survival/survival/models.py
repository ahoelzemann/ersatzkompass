from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.name)

class Unit(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.name)

class Collection(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.name)

class Item(models.Model):
    name = models.CharField(max_length=100)
    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    collections = models.ManyToManyField(Collection)

    def __str__(self):
        return "%s" % (self.name)