from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Item, Category, Substitution, Comment, Subcategory
from random import *
from django.db.models import Q

# Create your views here.
def home(request):
    items = Item.objects.order_by('?')[:4]
    context = {
        'categories': Category.objects.all(),
        'items': items,
    }
    return render(request, 'survival/home.html', context)

def categories(request):
    paginator = Paginator(Category.objects.all(), 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'categories': Category.objects.all(),
    }
    return render(request, 'survival/categories.html', context)

class CommentCreateView(CreateView):
    model = Comment
    fields = ['name', 'text']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['substitution'] = Substitution.objects.all()
        return context

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

class SearchResultsView(ListView):
    model = Item
    template_name = 'items.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        items = Item.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return items

def items(request):
    items = Item.objects.all()
    substitutions = Substitution.objects.all()
    item_list = []
    for substitution in substitutions:
        for item in items:
            if item.id == substitution.item_missing.id:
                if(item not in item_list):
                    item_list.append(item)
    paginator = Paginator(item_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'categories': Category.objects.all(),
    }
    return render(request, 'survival/items.html', context)

def items_sorted(request, subcategory_id):
    paginator = Paginator(Item.objects.filter(subcategory_id=subcategory_id), 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
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