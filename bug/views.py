from django.shortcuts import render, reverse, redirect
from django.views import generic
from .models import Bug, Image
from django.utils import timezone
from django.urls import reverse_lazy
from .forms import *
# from django.forms import modelformset_factory
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponseRedirect
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth import get_user_model

class FormActionMixin(object):

    def post(self, request, *args, **kwargs):
        """Add 'Cancel' button redirect."""
        if "cancel" in request.POST:
            return HttpResponseRedirect(reverse('bug:index'))
        else:
            return super(FormActionMixin, self).post(request, *args, **kwargs)
# Create your views here.
class IndexView(LoginRequiredMixin,generic.ListView):
    model= Bug
    template_name = 'bug/index.html'
    context_object_name = 'latest_bug_list'

    def get_queryset(self):
        """
        Return last five of bugs
        """
        return Bug.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]

class DeleteBug(LoginRequiredMixin,generic.DeleteView):
    model = Bug
    template_name ='bug/bug_delete.html'
    success_url = reverse_lazy('bug:index')

class DetailBug(LoginRequiredMixin,generic.DetailView):
    model = Bug
    template_name = 'bug/bug_details.html'

class UpdateBug(LoginRequiredMixin,generic.edit.UpdateView):
    model=Bug
    template_name = 'bug/bug_update.html'
    form_class= BugForm
    # fields = ['bug_title', 'bug_description', 'image']
    # success_url =  reverse_lazy('bug:index')

    def get_context_data(self, **kwargs):
        print("retrieve context data")

        context =  super(UpdateBug,self).get_context_data(**kwargs)
        if self.request.POST:
            context['image'] = ImageFormSet(self.request.POST,self.request.FILES, prefix='has_image', instance=self.object)
        else:
            context['image'] = ImageFormSet(instance=self.object)
        return context

    def form_valid(self,form):
        print("in form valid for update")
        context = self.get_context_data()
        images = context['image']
        with transaction.atomic():
            form.instance.reported_by =self.request.user
            self.object =  form.save()
            if images.is_valid():
                images.instance = self.object
                images.save()
        return super(UpdateBug,self).form_valid(form)

    def form_invalid(self, form):
        print(form)
        return super(UpdateBug,self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('bug:bug-detail', kwargs={'pk': self.object.pk})

class BugCreate(FormActionMixin,LoginRequiredMixin,generic.edit.CreateView):
    model =  Bug
    template_name = 'bug/bug_create.html'
    form_class = BugForm
    success_url= None

    def get_context_data(self, **kwargs):
        print("retrieve context data")
        context =  super(BugCreate,self).get_context_data(**kwargs)
        if self.request.POST:
            context['image'] = ImageFormSet(self.request.POST,self.request.FILES, prefix='has_image',queryset=Image.objects.none())
        else:
            context['image'] = ImageFormSet()
        return context

    def form_valid(self,form):
        print("in form valid for update")
        context = self.get_context_data()
        images = context['image']
        with transaction.atomic():
            form.instance.reported_by =self.request.user
            self.object =  form.save()
            if images.is_valid():
                images.instance = self.object
                images.save()
        return super(BugCreate,self).form_valid(form)

    def form_invalid(self, form):
        print(form)
        return super(BugCreate,self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('bug:bug-detail', kwargs={'pk': self.object.pk})




# https://dev.to/zxenia/django-inline-formsets-with-class-based-views-and-crispy-forms-14o6
# https://medium.com/@adandan01/django-inline-formsets-example-mybook-420cc4b6225d
