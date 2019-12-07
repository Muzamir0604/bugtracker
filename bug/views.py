from django.shortcuts import render, reverse, redirect
from django.views import generic
from .models import Bug
from django.utils import timezone

from .forms import BugForm
# from django.contrib.auth import get_user_model


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'bug/index.html'
    context_object_name = 'latest_bug_list'

    def get_queryset(self):
        """
        Return last five of bugs
        """
        return Bug.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]

def BugFormView(request):
    # user = get_user_model()
    if (request.method=='POST' and request.user.is_authenticated):
            form = BugForm(request.POST)
            if form.is_valid():
                title= form.cleaned_data['bug_title']
                description = form.cleaned_data['bug_description']
                pub_date =  timezone.now()
                print(title, description, pub_date, request.user)
                Bug.objects.create(**form.cleaned_data,pub_date=pub_date, reported_by= request.user)
                return redirect(reverse('bug:index'))


    form = BugForm()
    return render(request,'bug/bug_create.html',{'form':form})

def bug_detail_view(request,id):
    obj = Bug.objects.get(id=id)
    context={
        'title': obj.bug_title,
        'desc':obj.bug_description,
        'date':obj.pub_date,
        'user': obj.reported_by
    }
    return render(request, "bug/bug_details.html", context)

# def snippet_detail(request):
#     if request.method=='POST':
#         form = SnippetForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#
#     form = SnippetForm()
#     return render(request,'bug/form.html',{'form':form})
