from .all_imports import *

class IndexView(LoginRequiredMixin,generic.ListView):
    model= Bug
    template_name = 'bug/index.html'
    context_object_name = 'latest_bug_list'

    def get_queryset(self):
        """
        Return last five of bugs
        """
        return Bug.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]
