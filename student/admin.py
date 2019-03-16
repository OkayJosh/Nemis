from django.contrib import admin
from .models import Student, Posting, Book, Literacy, Attendance, Incentive, Appraisal, Numeracy, Parent

# Register your models here.
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Posting)
admin.site.register(Book)
admin.site.register(Literacy)
admin.site.register(Numeracy)
admin.site.register(Attendance)
admin.site.register(Incentive)
admin.site.register(Appraisal)