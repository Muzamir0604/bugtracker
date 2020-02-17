from django.contrib import admin
from .models import  Bug, Image, Team, Request
# Register your models here.
## Testing Rules Admin
# from bug.models import Bug
from rules.contrib.admin import ObjectPermissionsModelAdmin

class BugAdmin(ObjectPermissionsModelAdmin):
    pass

admin.site.register(Bug,BugAdmin)
admin.site.register(Image)
admin.site.register(Team)
admin.site.register(Request)
