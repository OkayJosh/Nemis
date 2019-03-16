from django.contrib import admin
from .models import Teacher, Posting, Employment, InHouseTraining, SkillSet, Appraisal

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Posting)
admin.site.register(Employment)
admin.site.register(InHouseTraining)
admin.site.register(SkillSet)
admin.site.register(Appraisal)