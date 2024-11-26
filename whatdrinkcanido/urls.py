"""
URL configuration for whatdrinkcanido project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import drink_detail, search_with_ingredients, search_by_name, search_with_ingredients_allow_missing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/drinks/<int:pk>/', drink_detail, name='drink_detail'),
    path('api/search_by_name/', search_by_name, name='search_by_name'),
    path('api/search_by_ingredients/', search_with_ingredients, name='search_with_ingredients'),
    path('api/search_by_ingredients_allow_missing/', search_with_ingredients_allow_missing, name='search_with_ingredients_allow_missing'),
]