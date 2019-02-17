from django.db import models

from utils.utils import CreationModificationDateMixin, UrlMixin, DateMixin, no_future
from teacher.models import STATE_CHOICES


class Asset(UrlMixin, CreationModificationDateMixin, DateMixin):
    name = models.CharField( max_length= 200)
    date_commissioned = models.DateField( blank=True)
    details = models.TextField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, null=True)
    value = models.IntegerField()
    expired_date = models.DateField()