from rest_framework import serializers
from .models import Project, SubProject, Members

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class SubProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubProject
        fields = '__all__'

class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'