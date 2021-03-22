from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('',views.IndexClassView.as_view(),name='index'),
    #path('category/<int:id>/', views.getProductsByCategory, name = 'category_products')
    path('category/<int:id>/', views.subcategoriesList,name='category_subcategory'),
]