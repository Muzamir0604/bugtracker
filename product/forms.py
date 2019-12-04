from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your title"}))
    email=forms.EmailField()
    description=forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder":"your description",
                "class": "new-class-name",
                "id":"my-id-for-textarea",
                "rows": 20,
                "cols":120,
                "label": "Description"
            }
        )
    )

    ## to override the cleaning
    ## create function "clean_<fieldname>"
    def clean_title(self, *args, **kwargs):
        title= self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("Not valid title")
        return title

    ## This is important to include for ModelForms
    class Meta:
        model = Product
        fields =[
            'title',
            'email',
            'description',
            'price'

        ]

class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={"placeholder":"Your title"}
    ))
    description=forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder":"your description",
                "class": "new-class-name",
                "id":"my-id-for-textarea",
                "rows": 20,
                "cols":120,
                "label": "Description"
            }
        )
    )
    price= forms.DecimalField()
