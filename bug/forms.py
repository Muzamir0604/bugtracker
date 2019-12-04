from django import forms
from .models import Snippet

class BugForm(forms.Form):
        title = forms.CharField(label="Title",max_length=200)
        description = forms.CharField(max_length=500)


class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields=('name', 'body')
