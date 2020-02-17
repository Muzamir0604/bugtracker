from .all_imports import *



class FormActionMixin(object):

    def post(self, request, *args, **kwargs):
        """Add 'Cancel' button redirect."""
        if "cancel" in request.POST:
            return HttpResponseRedirect(reverse('bug:index'))
        else:
            return super(FormActionMixin, self).post(request, *args, **kwargs)
# Create your views here.

class BugCreate(FormActionMixin,LoginRequiredMixin,generic.edit.CreateView):
    model =  Bug
    template_name = 'bug/bug_create.html'
    form_class = BugForm
    success_url= None

    def get_context_data(self, **kwargs):
        context =  super(BugCreate,self).get_context_data(**kwargs)
        if self.request.POST:
            context['image'] = ImageFormSet(self.request.POST,self.request.FILES, prefix='has_image',queryset=Image.objects.none())
            # context['bug_team'] = TeamForm(self.request.POST)
        else:
            context['image'] = ImageFormSet()
        return context

    def form_valid(self,form):
        context = self.get_context_data()
        images = context['image']
        bug = context['bug_team']
        with transaction.atomic():
            form.instance.reported_by =self.request.user
            self.object =  form.save()
            if images.is_valid():
                images.instance = self.object
                images.save()
            # if bug.is_valid():
            #     bug.instance = self.object
            #     bug.save()
        return super(BugCreate,self).form_valid(form)

    def form_invalid(self, form):
        print(form)
        return super(BugCreate,self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('bug:bug-detail', kwargs={'pk': self.object.pk})
