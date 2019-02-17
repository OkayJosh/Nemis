from rest_framework import viewsets
from .models import Student, Posting, Book, Literacy, Attendance, Feeding, Appraisal
from .serializers import StudentSerializer, PostingSerializer,  BookSerializer, LiteracySerializer, AttendanceSerializer, FeedingSerializer, AppraisalSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class PostingViewSet(viewsets.ModelViewSet):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class LiteracyViewSet(viewsets.ModelViewSet):
    queryset = Literacy.objects.all()
    serializer_class = LiteracySerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class FeedingViewSet(viewsets.ModelViewSet):
    queryset = Feeding.objects.all()
    serializer_class = FeedingSerializer

class AppraisalViewSet(viewsets.ModelViewSet):
    queryset = Appraisal.objects.all()
    serializer_class = AppraisalSerializer