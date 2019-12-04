from django.shortcuts import render
from .forms import RawProductForm, ProductForm
from .models import Product

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
