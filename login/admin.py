from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import GeneralAdminProfile, SupervisorAdminProfile, TeacherAdminProfile

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class GeneralAdminProfileInline(admin.StackedInline):
    model = GeneralAdminProfile
    can_delete = False

class SupervisorAdminProfileInline(admin.StackedInline):
    model = SupervisorAdminProfile
    can_delete = False

class TeacherAdminProfileInline(admin.StackedInline):
    model = TeacherAdminProfile
    can_delete = False


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (GeneralAdminProfileInline, SupervisorAdminProfileInline, TeacherAdminProfileInline)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)