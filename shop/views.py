from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from . import models as models
from django.template import loader

from .models import Category


class IndexClassView(ListView):
    model = models.Category
    template_name = 'shop/index.html'
    context_object_name = 'category_list'


class ProductsClassView(ListView):
    model = models.Product
    template_name = 'shop/Product.html'
    context_object_name = 'product_list'


class SubcategoriesClassView(ListView):
    template_name = 'shop/Subcategories.html'
    queryset = Category.objects.prefetch_related("subcategories")


def subcategoriesList(request, id):
    category = models.SubCategories.objects.get(category_id=id)
    context = {'category': category}
    return render(request, 'shop/Subcategories.html', context)
