from django.shortcuts import render, reverse, redirect
from django.views import generic
from .models import Bug, Image
from django.utils import timezone
from django.urls import reverse_lazy
from .forms import BugForm, ImageForm
from django.forms import modelformset_factory
from django.contrib import messages
# from django.contrib.auth import get_user_model


# Create your views here.
class IndexView(generic.ListView):
    # model= Bug
    template_name = 'bug/index.html'
    context_object_name = 'latest_bug_list'

    def get_queryset(self):
        """
        Return last five of bugs
        """
        return Bug.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]

class DeleteBug(generic.DeleteView):
    model = Bug
    template_name ='bug/bug_delete.html'
    success_url = reverse_lazy('bug:index')

class DetailBug(generic.DetailView):
    model = Bug
    template_name = 'bug/bug_details.html'

class UpdateBug(generic.UpdateView):
    model=Bug
    template_name = 'bug/bug_update.html'
    fields = ['bug_title', 'bug_description']
    success_url =  reverse_lazy('bug:index')

def BugFormView(request):

    ImageFormSet = modelformset_factory(Image,
                                        form=ImageForm, extra=3)

    if request.method == 'POST':

        bugForm = BugForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Image.objects.none())


        if bugForm.is_valid() and formset.is_valid():
            bug_form = bugForm.save(commit=False)
            bug_form.user = request.user
            bug_form.save()

            for form in formset.cleaned_data:
                print(form)
                image = form.get('image')
                photo = Image(bug=bug_form, image=image)
                photo.save()
            messages.success(request,
                             "Posted!")
            return redirect(reverse_lazy('bug:index'))
        else:

            print(bugForm.errors, formset.errors)
    else:
        bugForm = BugForm()
        formset = ImageFormSet(queryset=Image.objects.none())
    return render(request, 'bug/bug_create.html',
                  {'bugForm': bugForm, 'formset': formset})
