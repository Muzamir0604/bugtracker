# from .all_imports import *
#
#
#
# class AssignBug(LoginRequiredMixin,generic.edit.CreateView):
#     model =  Team
#     template_name = 'bug/bug_assign.html'
#     form_class = BugForm
#     success_url= None
#
#     def get_context_data(self, **kwargs):
#         print("retrieve context data")
#         context =  super(AssignBug,self).get_context_data(**kwargs)
#         if self.request.POST:
#             context['image'] = ImageFormSet(self.request.POST,self.request.FILES, prefix='has_image',queryset=Image.objects.none())
#         else:
#             context['image'] = ImageFormSet()
#         return context
#
#     def form_valid(self,form):
#         print("in form valid for update")
#         context = self.get_context_data()
#         images = context['image']
#         with transaction.atomic():
#             form.instance.reported_by =self.request.user
#             self.object =  form.save()
#             if images.is_valid():
#                 images.instance = self.object
#                 images.save()
#         return super(BugCreate,self).form_valid(form)
#
#     def form_invalid(self, form):
#         print(form)
#         return super(BugCreate,self).form_invalid(form)
#
#     def get_success_url(self):
#         return reverse_lazy('bug:bug-detail', kwargs={'pk': self.object.pk})
