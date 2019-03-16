from rest_framework import viewsets
from .models import Teacher, Posting, Employment, InHouseTraining, SkillSet, Appraisal
from .serializers import TeacherSerializer, PostingSerializer,  EmploymentSerializer, InHouseTrainingSerializer, SkillSetSerializer, AppraisalSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer

class EmploymentViewSet(viewsets.ModelViewSet):
    queryset = Employment.objects.all()
    serializer_class = EmploymentSerializer

class InHouseTrainingViewSet(viewsets.ModelViewSet):
    queryset = InHouseTraining.objects.all()
    serializer_class = InHouseTrainingSerializer

class SkillSetViewSet(viewsets.ModelViewSet):
    queryset = SkillSet.objects.all()
    serializer_class = SkillSetSerializer

class AppraiseViewSet(viewsets.ModelViewSet):
    queryset = Appraisal.objects.all()
    serializer_class = AppraisalSerializer