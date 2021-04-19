from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('',views.IndexClassView.as_view(),name='index'),
    #path('category/<int:id>/', views.getProductsByCategory, name = 'category_products')
    path('category/<int:id>/', views.subcategoriesList,name='category_subcategory'),
    path('suppliers/', views.SupplierClassView.as_view(),name='suppliers'),
    path('allProducts/', views.ProductsClassView.as_view(),name='all_products'),
    path('details/<int:id>/', views.editProduct,name='edit_product'),
    path('add_product/', views.CreateProduct.as_view(), name = 'add_product'),
    path('delete_product/<int:id>',views.delete_product,name='delete_product'),
    path('search/', views.search_product, name='search_product'),
    path('add_supplier/',views.create_supplier, name='create_supplier')
]