from operator import imod
from django.urls import path, include
from .views import *

urlpatterns = [
    path('check/',checkpdf),
    path('pdf_gen', pdf_gen, name='pdf_gen'),
    path('category/<str:slug>/', product_by_category , name='product-by-category'),
]