from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='cs-home'),
    path('items/', views.items, name='cs-items'),
    path('items/sorted/<int:subcategory_id>', views.items_sorted, name='cs-items-sorted'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='item-detail'),
    path('categories/', views.categories, name='cs-categories'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('substitutions/', views.substitutions, name='cs-substitutions'),
    path('login/', auth_views.LoginView.as_view(template_name='survival/login.html'), name='login'),
    path('admin2/', views.admin, name='cs-admin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='survival/logout.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)