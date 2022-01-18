from django.forms import fields
from rest_framework import serializers
from .models import Departments

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'