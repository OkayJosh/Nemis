import os
from django.db import models
from django.utils.timezone import now as timezone_now

from django.contrib.auth.models import User
from school.models import School

from utils.utils import CreationModificationDateMixin, UrlMixin, DateMixin, no_future


class Teacher(UrlMixin, CreationModificationDateMixin, DateMixin ):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    government_code = models.CharField(max_length=100)
    identification_number = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    telphone_number = models.IntegerField()
    email_address = models.EmailField()
    address = models.CharField(max_length=200, default='address')
    city = models.CharField(max_length=100, default='city')
    state_origin = models.CharField(max_length=20, null=True)
    state_residence = models.CharField(max_length=20, null=True)
    local_gov_origin = models.CharField(max_length=20, null=True)
    local_gov_residence = models.CharField(max_length=20, null=True)
    date_of_birth = models.DateField(blank=True, null=True, validators=[no_future])
    
    reason_for_change_of_employment = models.CharField()
    
    #previous employer details
    name_of_employer = models.CharField(max_length=100, null=True)
    date_of_registration = models.CharField(max_length=100, null=True)
    last_position_held = models.CharField(max_length=20, null=True)

     picture = models.ImageField(("Picture"), upload_to=upload_to,blank=True,null=True)

    def __str__(self):
        return full_name


class Employment(UrlMixin, CreationModificationDateMixin, DateMixin ):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, null=True, blank=True)

    date_of_empl = models.DateField("Date of Employment")
    postion_held = models.CharField(max_length=100)
    end_of_employment = models.DateField("End of Employment")

    def __str__(self):
        return self.postion_held

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
    participation = models.TextField("Describe the Teachers Participation", null=True)
    description_of_tranning = models.TextField("Describe the tranning in respect to the teacher", blank=True, null=True)
    date_of_training = models.DateField("Date of Tranning")

    def __str__(self):
        return self.name_of_tranning

class SkillSet(UrlMixin, CreationModificationDateMixin, DateMixin):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

    name_of_skill = models.CharField(max_length=100)
    date_of_skill = models.DateField("Date of Skill Aquizition", validators=[no_future])
    description_of_skill = models.TextField("Description of Skill", null=True)

    def __str__(self):
        return self.name_of_skill

class Appraisal(UrlMixin, CreationModificationDateMixin, DateMixin):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

    reason = models.TextField("Reason for Apraisal", null=True, blank=True)
    preaparedness = models.TextField("How prepared is the teacher", null=True)
    instructional = models.TextField("Use of instructional teaching Methods", null=True)
    class_environment = models.TextField("Describe the teacher teaching Environment", null=True)
    professionalism = models.TextField("How professional is the Teacher", null=True)
    date = models.DateField("Date due", validators=[no_future])

    def __str__(self):
        return self.amount


