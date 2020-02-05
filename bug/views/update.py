from .all_imports import *

class UpdateBug(LoginRequiredMixin,generic.edit.UpdateView):
    model=Bug
    template_name = 'bug/bug_update.html'
    form_class= BugForm

    # fields = ['bug_title', 'bug_description', 'image']
    # success_url =  reverse_lazy('bug:index')

    def get_context_data(self, **kwargs):
        print("retrieve context data")

        context =  super(UpdateBug,self).get_context_data(**kwargs)
        if self.request.POST:
            context['image'] = ImageFormSet(self.request.POST,self.request.FILES, prefix='has_image', instance=self.object)
        else:
            context['image'] = ImageFormSet(instance=self.object)
        return context

    def form_valid(self,form):
        print("in form valid for update")
        context = self.get_context_data()
        images = context['image']
        with transaction.atomic():
            form.instance.reported_by =self.request.user
            self.object =  form.save()
            if images.is_valid():
                images.instance = self.object
                images.save()
        return super(UpdateBug,self).form_valid(form)

    def form_invalid(self, form):
        print(form)
        return super(UpdateBug,self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('bug:bug-detail', kwargs={'pk': self.object.pk})
