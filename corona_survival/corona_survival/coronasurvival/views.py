from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Item, Unit, Collection, Category

# Create your views here.
def home(request):
    context = {
        'items': Item.objects.all(),
        'title':'Corona Survival'
    }
    return render(request, 'coronasurvival/home.html', context)

@login_required
def admin(request):
    context = {
        'title':'Admin page'
    }
    return render(request, 'coronasurvival/admin.html', context)