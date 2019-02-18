import os
from django.db import models
from django.utils.timezone import now as timezone_now

from django.contrib.auth.models import User
from school.models import School

from utils.utils import CreationModificationDateMixin, UrlMixin, DateMixin, no_future


class Teacher(UrlMixin, CreationModificationDateMixin, DateMixin ):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField( max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, default='address')
    city = models.CharField(max_length=100, default='city')
    state = models.CharField(max_length=20, null=True)
    date_of_birth = models.DateField(blank=True, null=True, validators=[no_future])

    # picture = models.ImageField(("Picture"),
    #             upload_to=upload_to,blank=True,null=True)

    def __str__(self):
        return '%s %s %s' % (self.last_name, self.first_name, self.middle_name)

    class Admin:
        list_dispaly = ["fist_name", "middle_name", "last_name", "address",
            "city"]

    list_filter =('state', 'date_of_birth')
    ordering = ('-created')
    search_fields = ('state')


class Employment(UrlMixin, CreationModificationDateMixin, DateMixin ):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, null=True, blank=True)

    date_of_empl = models.DateField("Date of Employment")
    postion_held = models.CharField(max_length=100)
    end_of_employment = models.DateField("End of Employment")

    def __str__(self):
        return self.name_of_school

class Posting( UrlMixin, CreationModificationDateMixin, DateMixin):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    assignment = models.TextField(null=True)
    date_of_posting = models.DateField("Date of Posting")


    def __str__(self):
        return '%s as %s' % (self.teacher, self.assignment)

class InHouseTraining(UrlMixin, CreationModificationDateMixin, DateMixin):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

    name_of_training = models.CharField(max_length=100)
    purpose_of_training = models.TextField("Purpose")
    location_of_training = models.CharField(max_length=100)
    date_of_training = models.DateField("Date of Tranning")

    def __str__(self):
        return self.name_of_tranning

class SkillSet(UrlMixin, CreationModificationDateMixin, DateMixin):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

    name_of_skill = models.CharField(max_length=100)
    date_of_skill = models.DateField("Date of Skill Aquizition", validators=[no_future])

    def __str__(self):
        return self.name_of_skill

class Appraisal(UrlMixin, CreationModificationDateMixin, DateMixin):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

    amount = models.IntegerField()
    reason = models.TextField(null=True, blank=True)
    date = models.DateField("Date due", validators=[no_future])

    def __str__(self):
        return self.amount


