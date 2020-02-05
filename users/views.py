# from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect

User = get_user_model()

# Create your views here.
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url =  reverse_lazy('home')
    template_name = 'signup.html'
    def form_valid(self, form):
        view =  super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view

class DetailProfile(generic.DetailView):
        model = User
        template_name = 'profile.html'

class EditProfile(generic.edit.UpdateView):

    form_class= CustomUserChangeForm
    # success_url = reverse_lazy('home')
    template_name = 'edit_profile.html'
    model = User
    #
    def get(self,request,pk):
        print(pk)
        self.object = User.objects.get(id=pk)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.user.pk})
