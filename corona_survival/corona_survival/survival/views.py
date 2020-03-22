from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Item, Category, Substitution
from random import *

# Create your views here.
def home(request):
    items = Item.objects.order_by('?')[:4]
    context = {
        'categories': Category.objects.all(),
        'items': items,
        'title': 'ErsatzKompass'
    }
    return render(request, 'survival/home.html', context)

def category(request):
    context = {
        'categories': Category.objects.all(),
        'title':'Corona Survival - Categories'
    }
    return render(request, 'survival/categories.html', context)

class ItemDetailView(DetailView):
    model = Item    

class CategoryDetailView(DetailView):
    model = Category

def item(request):
    context = {
        'items': Item.objects.all(),
        'categories': Category.objects.all(),
        'title':'Items'
    }
    return render(request, 'survival/items.html', context)

def substitution(request):
    context = {
        'categories': Category.objects.all(),
        'substitutions': Substitution.objects.all(),
        'title':'Substitutions'
    }
    return render(request, 'survival/substitutions.html', context)

@login_required
def admin(request):
    context = {
        'items': Item.objects.all(),
        'categories': Category.objects.all(),
        'subcategories': Item.objects.all(),
        'substitutions': Substitution.objects.all(),
        'title':'Admin page'
    }
    return render(request, 'survival/admin.html', context)