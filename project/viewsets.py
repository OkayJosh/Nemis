from rest_framework import viewsets
from .models import Project, SubProject, Members
from .serializers import ProjectSerializer, SubProjectSerializer, MembersSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SubProjectViewSet(viewsets.ModelViewSet):
    queryset = SubProject.objects.all()
    serializer_class = SubProjectSerializer

class MembersViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer