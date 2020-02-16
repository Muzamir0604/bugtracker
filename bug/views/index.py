from .all_imports import *

class IndexView(LoginRequiredMixin,generic.ListView):
    model= Bug
    template_name = 'bug/index.html'
    paginate_by= 10
    context_object_name = 'latest_bug_list'
    #
    def get_queryset(self):
        """
        return : For Supervisor: return all ordered by latest date
                For Analysts + reporters:  return all reported by latest date
        """
        if self.request.user.groups.all()[0].name=="Supervisors":
            return Bug.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
        else:
            return Bug.objects.filter(reported_by=self.request.user).order_by('-pub_date')
