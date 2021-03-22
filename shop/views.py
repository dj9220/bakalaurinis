from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from . import models as models
from django.template import loader
# Create your views here.

class IndexClassView(ListView):
    model = models.Category
    template_name = 'shop/index.html'
    context_object_name = 'category_list'

class ProductsClassView(ListView):
    model = models.Product
    template_name = 'shop/Product.html'
    context_object_name = 'product_list'


class SubcategoriesClassView(ListView):
    model = models.SubCategories
    template_name = 'shop/Subcategories.html'

    def get(self, request, *args, **kwargs):
        kwargs['subs'] = models.SubCategories.objects.filter(category__name=models.Category.name)

    def get_context_data(self, **kwargs):
        context = super(SubcategoriesClassView,self).get_context_data(**kwargs)
        category = models.SubCategories.category
        subcategory = models.SubCategories.objects.filter(categories=category)
        context['subcategories'] = subcategory
        print(context['subcategories'])
        return context
def subcategoriesList(request,id):
    category = models.SubCategories.objects.get(category_id=id)
    context = {'category':category}
    return render(request,'shop/Subcategories.html',context)









