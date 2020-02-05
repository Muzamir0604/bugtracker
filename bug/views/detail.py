from .all_imports import *

class DetailBug(LoginRequiredMixin,generic.DetailView):
    model = Bug
    template_name = 'bug/bug_details.html'
