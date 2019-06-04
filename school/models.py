from django.db import models
from utils.models import CreationModificationDateMixin, UrlMixin, DateMixin, no_future
from django.contrib.auth.models import User


class School(CreationModificationDateMixin, UrlMixin, DateMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20, null=True)
    date_of_creation = models.DateField( null=True, validators=[no_future])

    def __str__(self):
        return '%s' % (self.name)

class Incident(CreationModificationDateMixin, UrlMixin, DateMixin):

    school = models.ForeignKey(School, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    details = models.TextField()
    action_taken = models.TextField()

    def __str__(self):
        return '%s' % (self.title)

class Extra_Curricular(CreationModificationDateMixin, UrlMixin, DateMixin):

    school = models.ForeignKey(School, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    details = models.TextField()

    def __str__(self):
        return '%s' % (self.title)
    
  class Asset(CreationModificationDateMixin, UrlMixin, DateMixin):

    school = models.ForeignKey(School, on_delete=models.CASCADE)
    type = models.CharField(max_length=200)
    nature = models.CharField(max_length=200)
    description= models.TextField()
    value = models.CharField(max_length=200)
    date_of_acquisition = models.DateField()

    def __str__(self):
        return '%s' % (self.nature)

 class AssetCondition (CreationModificationDateMixin, UrlMixin, DateMixin):

    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    assesor = models.CharField(max_length=200)
    condition = models.TextField()
    remark = models.TextField()
    

    def __str__(self):
        return '%s' % (self.nature)
