# from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login


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
