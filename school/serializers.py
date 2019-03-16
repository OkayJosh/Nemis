from rest_framework import serializers
from .models import School, Incident, Extra_Curricular

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'

class Extra_CurricularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra_Curricular
        fields = '__all__'
