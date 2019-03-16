from django.db import models
from utils.models import CreationModificationDateMixin, UrlMixin, DateMixin, no_future

from login.models import GeneralAdminProfile
from school.models import School
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Student(UrlMixin, CreationModificationDateMixin, DateMixin ):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField( max_length=100)
    last_name = models.CharField(max_length=100)
    pics = models.ImageField(default='default.jpg')
    address = models.CharField(max_length=200, default='address')
    city = models.CharField(max_length=100, default='city')
    local_government_origin = models.CharField(max_length=20, null=True, default='local origin')
    state_origin = models.CharField(max_length=20, null=True, default='state origin')
    local_government_residence = models.CharField(max_length=20, null=True, default='local residence')
    state_residence = models.CharField(max_length=20, null=True, default='state residence')
    date_of_birth = models.DateField(blank=True, null=True, validators=[no_future])

    def __str__(self):
        return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)

class Parent(UrlMixin, CreationModificationDateMixin, DateMixin ):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField( max_length=100)
    last_name = models.CharField(max_length=100)
    pics = models.ImageField(default='default.jpg')
    address = models.CharField(max_length=200, default='address')
    city = models.CharField(max_length=100, default='city')
    local_government_origin = models.CharField(max_length=20, null=True)
    state_origin = models.CharField(max_length=20, null=True)
    local_government_residence = models.CharField(max_length=20, null=True)
    state_residence = models.CharField(max_length=20, null=True)
    date_of_birth = models.DateField(blank=True, null=True, validators=[no_future])

    def __str__(self):
        return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)

class Book(UrlMixin, CreationModificationDateMixin, DateMixin):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    name_of_book = models.CharField(max_length=255)
    ISDN_of_book = models.CharField(max_length=255, null=True, default="ISDN")
    purpose_of_the_book = models.CharField(max_length=255, null=True)

    def __str__(self):
        return '%s for %s' % (self.name_of_book, self.student)


class Literacy(UrlMixin, CreationModificationDateMixin, DateMixin):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    literacy = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], default="3")
    describe_literacy = models.TextField("Describe the Literacy of the Student", null=True)

    def __str__(self):
        return 'Literacy details for %s' % (self.student)

class Numeracy(UrlMixin, CreationModificationDateMixin, DateMixin):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    numeracy = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    describe_numeracy = models.TextField("Describe the Literacy of the Student", null=True)

    def __str__(self):
        return 'Numeracy details for %s' % (self.student)


class Attendance(UrlMixin, CreationModificationDateMixin, DateMixin):

    # Many attendance will belong to one student
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True)
    present = models.BooleanField()

    def __str__(self):
        return '%s is %s' % (self.student, self.present)

    
class Incentive(UrlMixin, CreationModificationDateMixin, DateMixin):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    description_of_incentive = models.TextField("Describing the incentives", null=True)
    date_of_inclusion = models.DateField(null=True)


class Appraisal(UrlMixin, CreationModificationDateMixin, DateMixin):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField("Name of Appraisal",max_length=255, null=True)
    method_of_appraisal = models.CharField(max_length=255, null=True)
    
    performance = models.TextField("Describing the Performance of the student", null=True)
    brief = models.TextField()

    def __str__(self):
        return '%s for %s' % (self.amount, self.student)


class Posting(UrlMixin, CreationModificationDateMixin, DateMixin):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    school = models.ForeignKey(School ,on_delete=models.CASCADE, null= True, related_name='studentPosting', blank=True)
    date_of_posting = models.DateField("Date of Posting", validators=[no_future])

    def __str__(self):
        return '%s posted to %s' % (self.student, self.name_of_school)




