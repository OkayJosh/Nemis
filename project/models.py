from django.db import models

from utils.models import CreationModificationDateMixin, UrlMixin, DateMixin, no_future
from django.contrib.auth.models import User

class Project(UrlMixin, CreationModificationDateMixin, DateMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField( max_length= 200)
    date_of_approval = models.DateField()
    details = models.TextField()
    funds = models.IntegerField()
    close_out_date = models.DateField()


    def __str__(self):
        return 'Project %s' % (self.name)

class SubProject (UrlMixin, CreationModificationDateMixin, DateMixin ):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    date_of_approval = models.DateField()
    details = models.TextField()
    funds = models.IntegerField()
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

    def __str__(self):
        return 'Member %s' % (self.name)