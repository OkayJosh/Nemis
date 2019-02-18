from django.db import models
from django.contrib.auth.models import User
from utils.models import CreationModificationDateMixin, UrlMixin, DateMixin

class Profile (models.Model):
    user = models.OneToOne()
