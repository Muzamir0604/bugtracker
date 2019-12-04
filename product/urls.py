from . import views
from django.urls import path

app_name = 'product'
urlpatterns = [
    path('',views.product_create_view, name='product-form'),
    path('<int:id>/delete/',views.product_delete_view, name = 'product-delete'),
    path('list/', views.product_list_view, name='product-list'),
    path('article/', views.ArticleListView.as_view(), name='article-list')
]
