from django.shortcuts import render, reverse, redirect
from django.views import generic
from ..models import Bug, Image
from django.utils import timezone
from django.urls import reverse_lazy
from ..forms import *
# from django.forms import modelformset_factory
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponseRedirect
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth import get_user_model







# https://dev.to/zxenia/django-inline-formsets-with-class-based-views-and-crispy-forms-14o6
# https://medium.com/@adandan01/django-inline-formsets-example-mybook-420cc4b6225d
