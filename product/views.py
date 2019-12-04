from django.shortcuts import render, get_object_or_404, redirect
from .forms import RawProductForm, ProductForm
from .models import Product, Article
from django.urls import reverse

from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

# Create your views here.
# def product_create_view(request):
#     my_form= RawProductForm()
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             ## the two stars change it to arguments
#             Products.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context={
#     "form": my_form
#     }
#     return render(request,"product/product_create.html", context)

def product_create_view(request):
    ## to initialize data to ModelForms
    initial_data={
        'title':"MY awesome title"
    }

    ## Note when you add this line, it will basically allow you to the object at id=1
    ## if this is not included, a new object will be created
    obj = Product.objects.get(id=1)

    form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
    if form.is_valid():
        form.save()
        form=ProductForm()

    context= {
        "form":form
    }
    return render(request,"product/product_create.html", context)

def product_delete_view(request, id):
    obj =  get_object_or_404(Product, id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('../../')
    context={
        "object":obj
    }
    return render(request,'product/product_delete.html',context)

def product_list_view(request):
    queryset = Product.objects.all()
    context={
        "object_list": queryset
    }
    return render(request, "product/product_list.html", context)

class ArticleListView(ListView):
    template_name="product/article_list.html"
    queryset= Article.objects.all() # product/article_list.html
