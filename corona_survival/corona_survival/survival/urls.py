from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='cs-home'),
    path('items/', views.item, name='cs-item'),
    path('categories/', views.category, name='cs-category'),
    path('substitutions/', views.substitution, name='cs-substitution'),
    path('login/', auth_views.LoginView.as_view(template_name='survival/login.html'), name='login'),
    path('admin2/', views.admin, name='cs-admin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='survival/logout.html'), name='logout'),
]