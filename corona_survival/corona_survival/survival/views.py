from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Item, Category, Substitution, Comment, Subcategory
from random import *

# Create your views here.
def home(request):
    items = Item.objects.order_by('?')[:4]
    context = {
        'categories': Category.objects.all(),
        'items': items,
    }
    return render(request, 'survival/home.html', context)

def categories(request):
    context = {
        'categories': Category.objects.all(),
    }
    return render(request, 'survival/categories.html', context)

#class CommentCreateView(CreateView):
#    model = Comment
#    fields = ['name', 'text']
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['categories'] = Substitution.objects.all()
#        return context

class ItemDetailView(DetailView):
    model = Item    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

def items(request):
    context = {
        'items': Item.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'survival/items.html', context)

def items_sorted(request, subcategory_id):
    items = Item.objects.filter(subcategory_id=subcategory_id)
    context = {
        'items': items,
        'categories': Category.objects.all(),
    }
    return render(request, 'survival/items.html', context)

def substitutions(request):
    context = {
        'categories': Category.objects.all(),
        'substitutions': Substitution.objects.all(),
    }
    return render(request, 'survival/substitutions.html', context)

@login_required
def admin(request):
    context = {
        'items': Item.objects.all(),
        'categories': Category.objects.all(),
        'subcategories': Item.objects.all(),
        'substitutions': Substitution.objects.all(),
    }
    return render(request, 'survival/admin.html', context)