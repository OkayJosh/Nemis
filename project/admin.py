from django.contrib import admin
from .models import Project, SubProject, Members
# Register your models here.

# class ProjectInline(admin.StackedInline):
#     model = Project
#     can_delete = False

# class SubProjectInline(admin.StackedInline):
#     model = SubProject
#     can_delete = False

# class MembersInline(admin.StackedInline):
#     model = Members
#     can_delete = False

# class ProjectBase(Project):
#     inlines = (ProjectInline, SubProjectInline, MembersInline)

admin.site.register(Project)
admin.site.register(SubProject)
admin.site.register(Members)