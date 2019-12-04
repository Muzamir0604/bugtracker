from . import views
from django.urls import path

app_name = 'product'
urlpatterns = [
    path('',views.product_create_view, name='product-form'),


]
