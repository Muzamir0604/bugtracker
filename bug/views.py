from django.shortcuts import render
from django.views import generic
from .models import Bug
from django.utils import timezone

from .forms import BugForm, SnippetForm


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'bug/index.html'
    context_object_name = 'latest_bug_list'

    def get_queryset(self):
        """
        Return last five of bugs
        """
        return Bug.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

def BugFormView(request):
    if request.method=='POST':
        form = BugForm(request.POST)
        if form.is_valid():
            title= form.cleaned_data['title']
            description = form.cleaned_data['description']
            print(title, description)


    form = BugForm()
    return render(request,'bug/form.html',{'form':form})


def snippet_detail(request):
    if request.method=='POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()


    form = SnippetForm()
    return render(request,'bug/form.html',{'form':form})
