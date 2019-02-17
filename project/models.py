from django.db import models

from utils.utils import CreationModificationDateMixin, UrlMixin, DateMixin, no_future


class Project(UrlMixin, CreationModificationDateMixin, DateMixin):
    name = models.CharField( max_length= 200)
    date_of_approval = models.DateField()
    details = models.TextField()
    appraisal = models.IntegerField()
    close_out_date = models.DateField()


    def __str__(self):
        return 'Project %s' % (self.name)

class SubProject (UrlMixin, CreationModificationDateMixin, DateMixin ):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    date_of_approval = models.DateField()
    details = models.TextField()
    appraisal = models.IntegerField()
    close_out_date = models.DateField()

    def __str__(self):
        return 'Project %s' % (self.name)

class Members(UrlMixin, CreationModificationDateMixin, DateMixin):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    position_held = models.CharField(max_length=100)
    details = models.TextField()