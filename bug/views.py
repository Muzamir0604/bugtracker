from django.shortcuts import render
from django.views import generic
from .models import Bug
from django.utils import timezone
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'bug/index.html'
    context_object_name = 'latest_bug_list'

    def get_queryset(self):
        """
        Return last five of bugs
        """
        return Bug.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
