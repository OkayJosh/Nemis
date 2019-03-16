from rest_framework import viewsets
from .models import School, Incident, Extra_Curricular
from .serializers import SchoolSerializer, IncidentSerializer,  Extra_CurricularSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

class Extra_CurricularViewSet(viewsets.ModelViewSet):
    queryset = Extra_Curricular.objects.all()
    serializer_class = Extra_CurricularSerializer