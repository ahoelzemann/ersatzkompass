from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Item, Category, Substitution

# Create your views here.
def home(request):
    context = {
        'items': Item.objects.all(),
        'title':'Corona Survival'
    }
    return render(request, 'survival/home.html', context)

def category(request):
    context = {
        'categories': Category.objects.all(),
        'title':'Corona Survival - Categories'
    }
    return render(request, 'survival/category.html', context)

def substitution(request):
    context = {
        'substitutions': Substitution.objects.all(),
        'title':'Corona Survival - Substitutions'
    }
    return render(request, 'survival/substitution.html', context)

@login_required
def admin(request):
    context = {
        'title':'Admin page'
    }
    return render(request, 'survival/admin.html', context)