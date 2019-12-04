from django.contrib import admin
from .models import Snippet, Bug
# Register your models here.

admin.site.register(Snippet)
admin.site.register(Bug)
