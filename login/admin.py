from django.contrib import admin

from .models import GeneralAdminProfile, SupervisorAdminProfile, TeacherAdminProfile

# Re-register UserAdmin
admin.site.register(GeneralAdminProfile)
admin.site.register(SupervisorAdminProfile)
admin.site.register(TeacherAdminProfile)