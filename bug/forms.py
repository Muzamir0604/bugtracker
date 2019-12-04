from django import forms
from .models import Bug
from django.utils import timezone

class BugForm(forms.ModelForm):
    bug_title = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder":"e.g Blue Screen and etc",
            "Label":"Name of Bug"
            }))
    bug_description = forms.CharField(
        required=False,
        widget=forms.Textarea(
                attrs={
                    "placeholder":"your description",
                    "id":"my-id-for-textarea",
                    "rows": 5,
                    "cols":10,
                    "label": "Description"}
            ))
        
    class Meta:
        model= Bug
        fields =[
            'bug_title',
            'bug_description'
            ]

# class SnippetForm(forms.ModelForm):
#
#     class Meta:
#         model = Snippet
#         fields=('name', 'body')
