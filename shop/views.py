from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView
from django.http import HttpResponse
from . import models as models
from django.template import loader
from . import forms as form
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
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
@login_required(login_url='users:login')
def editProduct(request,id):
    product = models.Product.objects.get(id=id)
    productForm = form.ProductForm(request.POST or None, instance=product)
    if productForm.is_valid():
        productForm.save()
        return redirect('shop:all_products')
    return render(request,'shop/Product form.html',{'form':productForm, 'product':product})

@login_required
def create_product(request):
    forms = form.ProductForm()
    if request.method=='POST':
        forms = form.ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
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
