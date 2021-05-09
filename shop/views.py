from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView
from django.http import HttpResponse
from . import models as models
from django.http import JsonResponse
from django.template import loader
from . import forms as form
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .serializers import ProductSerializer
import json
from django.contrib import messages
# Create your views here.

class IndexClassView(ListView):
    model = models.Category
    template_name = 'shop/index.html'
    context_object_name = 'category_list'

class ProductsClassView(ListView):
    model = models.Product
    template_name = 'shop/Product.html'
    context_object_name = 'product_list'


class SupplierClassView(ListView):
    model = models.Supplier
    template_name = 'shop/Supplier.html'
    context_object_name = 'supplier_list'


def subcategoriesList(request,id):
    category = models.SubCategories.objects.filter(category_id=id)
    context= {'category':category}
    return render(request,'shop/Subcategories.html',context)
def products_by_subcategory(request, id):
    product = models.Product.objects.filter(subCategory_id=id)
    return render(request, 'shop/productSubcategory.html',{'products':product})
@login_required(login_url='users:login')
def editProduct(request,id):
    product = models.Product.objects.get(id=id)
    productForm = form.ProductForm(request.POST or None, instance=product)
    if productForm.is_valid():
        productForm.save()
        messages.add_message(request,f'Produktas {product.name} sėkmingai pakeistas')
        return redirect('shop:all_products')
    return render(request,'shop/Product form.html',{'form':productForm, 'product':product})

@login_required
def create_product(request):
    forms = form.ProductForm()
    if request.method=='POST':
        forms = form.ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            name = forms.cleaned_data.get('name')
            messages.success(request,f'Produktas {name} pridėtas')
            return redirect('shop:all_products')
    return render(request, 'shop/Product form.html', {'form': forms})

@login_required(login_url='users:login')
def delete_product(request,id):
    product = models.Product.objects.get(id=id)
    if request.method=='POST':
        product.delete()
        return redirect('shop:all_products')
    return render(request,'shop/delete-product.html', {'product':product})

def search_product(request):
    if request.method == 'POST':
        query_name = request.POST.get('name', None)
        if query_name:
            results = models.Product.objects.filter(name__icontains=query_name)
            return render(request, 'shop/product-search.html', {'results':results})
        return render(request,'shop/product-search.html')

@login_required(login_url='users:login')
def create_supplier(request):
    forms = form.SupplierForm()
    if request.method == 'POST':
        forms = form.SupplierForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('shop:suppliers')
    return render(request,'shop/SupplierForm.html',{'form':forms})
@login_required
def SendMail(request, id):
    supp = models.Supplier.objects.get(id=id)
    if request.method=='GET':
        forms=form.SendEmailForm()
    else:
        forms =form.SendEmailForm(request.POST)
        if forms.is_valid():
            fromemail = supp.email
            subject = forms.cleaned_data['subject']
            message = forms.cleaned_data['message']
            send_mail(subject,message,fromemail,[supp.email,fromemail])
    return render(request,'shop/Email-page.html', {'form':forms})

@login_required
def edit_productQuantity(request, id):
    requestData = json.loads(request.body)
    product = models.Product.objects.get(id=id)
    productSerializer = ProductSerializer(data=product, instance=requestData)
    print(requestData)

    if productSerializer.is_valid():
        result = productSerializer.save()
        return JsonResponse(result.data)
    return JsonResponse({'error':'failed'}, status=400)
@login_required
def product_in_catalog(request, id):
    product = models.Product.objects.get(id=id)
    return render(request, 'shop/product_in_catalog.html.html', {'product':product})


