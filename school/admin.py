from django.contrib import admin
from .models import School, Incident, Extra_Curricular

# Register your models here.
admin.site.register(School)
admin.site.register(Incident)
admin.site.register(Extra_Curricular)