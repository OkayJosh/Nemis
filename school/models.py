from django.db import models
from utils.models import CreationModificationDateMixin, UrlMixin, DateMixin, no_future

from teacher.models import Teacher, STATE_CHOICES
from student.models import Student
from asset.models import Asset
from project.models import Project

class School(CreationModificationDateMixin, UrlMixin, DateMixin):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20, choices=STATE_CHOICES)
    date_of_creation = models.DateField( null=True, validators=[no_future])
    #A school has many teachers, students, assets, and projets
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.name)

class Incident(CreationModificationDateMixin, UrlMixin, DateMixin):

    school = models.ForeignKey(School, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    details = models.TextField()

    def __str__(self):
        return '%s' % (self.title)

class Extra_Curricular(CreationModificationDateMixin, UrlMixin, DateMixin):

    school = models.ForeignKey(School, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    details = models.TextField()

    def __str__(self):
        return '%s' % (self.title)
