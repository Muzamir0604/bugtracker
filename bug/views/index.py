from .all_imports import *



# set basic config for logging
logging.basicConfig(filename='logs/'+__name__+'.log',level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(filename)s:%(message)s')
logger = logging.getLogger(__name__)

class IndexView(LoginRequiredMixin,generic.ListView):
    logger.debug('Index - LogIn Success')
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
        logger.debug(' current user: {} & group: {}'.format(self.request.user, self.request.user.groups.all()[0]))
        if self.request.user.groups.all()[0].name=="Supervisors":
            logger.debug("Supervisor object returned")
            return Bug.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
        else:
            logger.debug("Other objects returned")
            return Bug.objects.filter(reported_by=self.request.user).order_by('-pub_date')


## TODO: adding filters https://www.youtube.com/watch?v=nle3u6Ww6Xk
