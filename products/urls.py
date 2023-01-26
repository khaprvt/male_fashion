from django.urls import path
from .views import ProductListView

app_name = 'products'

urlpatterns = [
    path('products/', ProductListView.as_view(), name='all'),
]