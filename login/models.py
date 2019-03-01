from django.db import models
from django.contrib.auth.models import User
from utils.models import CreationModificationDateMixin, UrlMixin, DateMixin
from django.contrib.auth.models import User
from school.models import School

class GeneralAdminProfile(UrlMixin, CreationModificationDateMixin, DateMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pics = models.ImageField(default='default')

    def __str__(self):
        return self.user.username + ' Profile'
    


class SupervisorAdminProfile(UrlMixin, CreationModificationDateMixin, DateMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True)

class TeacherAdminProfile(UrlMixin, CreationModificationDateMixin, DateMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True)
