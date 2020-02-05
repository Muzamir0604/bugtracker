from .all_imports import *

class DeleteBug(LoginRequiredMixin,generic.DeleteView):
    model = Bug
    template_name ='bug/bug_delete.html'
    success_url = reverse_lazy('bug:index')
