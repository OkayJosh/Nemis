from django.db import models
from utils.models import CreationModificationDateMixin, UrlMixin, DateMixin, no_future

from teacher.models import STATE_CHOICES
# teacher model was imported to have access to state choices

#from school.models import School
# institution model was imported to link student to istitution as well as to have access to ministries of education



class Student(UrlMixin, CreationModificationDateMixin, DateMixin ):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField( max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, default='address')
    city = models.CharField(max_length=100, default='city')
    state = models.CharField(max_length=20, choices=STATE_CHOICES, null=True)
    date_of_birth = models.DateField(blank=True, null=True, validators=[no_future])
    #belongs_to =models.CharField(max_length=10, choices=MIN_EDU, null=True)


    academic_text = models.TextField(blank=True,null=True)

    moral_text = models.TextField(blank=True,null=True)

    def __str__(self):
        return 'FGN/%s' % (self.id)

class Book(UrlMixin, CreationModificationDateMixin, DateMixin):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name_of_book = models.CharField(max_length=255)

    def __str__(self):
        return '%s for %s' % (self.name_of_book, self.student)


class Literacy(UrlMixin, CreationModificationDateMixin, DateMixin):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    english_literacy = models.CharField(max_length=255)
    numeracy = models.CharField(max_length=255)

    def __str__(self):
        return 'Literacy details for %s' % (self.student)


class Attendance(UrlMixin, CreationModificationDateMixin, DateMixin):

    # Many attendance will belong to one student
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    present = models.BooleanField()



    # def out_of_school():
    #     # get the total number of time absent to calculate out of school

    # def return_to_school():
    #     # After the streak of absence, is present true?
    def __str__(self):
        return '%s is %s' % (self.student, self.present)


class Feeding(UrlMixin, CreationModificationDateMixin, DateMixin):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    feeding = models.BooleanField()

    def __str__(self):
        return '%s %s' % (self.student, self.feeding)


class Appraisal(UrlMixin, CreationModificationDateMixin, DateMixin):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.IntegerField()
    brief = models.TextField()

    def __str__(self):
        return '%s for %s' % (self.amount, self.student)


class Posting(UrlMixin, CreationModificationDateMixin, DateMixin):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    #school = models.OneToOneField(School ,on_delete=models.CASCADE, null= True)
    date_of_posting = models.DateField("Date of Posting", validators=[no_future])

    def __str__(self):
        return '%s posted to %s' % (self.student, self.name_of_school)




