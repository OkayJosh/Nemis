from urllib.parse import urlparse, urlunparse

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from datetime import date
from django.core.exceptions import ValidationError

class CreationModificationDateMixin(models.Model):
    """
    Abstract base class with a creation
    and modification date and time
    
    """
    class Meta:
        abstract = True

    created = models.DateTimeField(
        _("creation date and time"),
        auto_now_add=True)
    updated = models.DateTimeField(
        _("modification date and time"),
        auto_now=True)




class UrlMixin(models.Model):
    """
    A replacement for get_absolute_url()
    Models extending this mixin should have
    either get_url or get_url_path implemented.
    """
    class Meta:
        abstract = True

    def get_url(self):
        if hasattr(self.get_url_path, "dont_recurse"):
            raise NotImplementedError
        try:
            path = self.get_url_path()
        except NotImplementedError:
            raise
        website_host = getattr(settings,
                               "SITE_HOST",
                               "localhost:8000")
        return f"http://{website_host}/{path}"
    get_url.dont_recurse = True

    def get_url_path(self):
        if hasattr(self.get_url, "dont_recurse"):
            raise NotImplementedError
        try:
            url = self.get_url()
        except NotImplementedError:
            raise
        bits = urlparse(url)
        return urlunparse(("", "") + bits[2:])
    get_url_path.dont_recurse = True

    def get_absolute_url(self):
        return self.get_url_path()

class DateMixin(models.Model):

    allow_future = False

    class Meta:
        abstract = True

def no_future(value):
    today = date.today()
    if value > today:
        raise ValidationError('Date of Birth cannot be today or in the future.')


