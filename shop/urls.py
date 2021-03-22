from django.urls import path
from . import views
from .views import SubcategoriesClassView

app_name = 'shop'
urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    # path('category/<int:id>/', views.getProductsByCategory, name = 'category_products')
    path('category/<int:id>/', views.subcategoriesList, name='category_subcategory'),
    path('categories/', SubcategoriesClassView.as_view(), name='category_subcategory'),
]
