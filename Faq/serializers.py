from rest_framework import serializers
from Organizations.serializers import DepartmentSerializer
from .models import Faq

class FaqSerializer(serializers.ModelSerializer):
    
    department = DepartmentSerializer
    class Meta:
        
        model = Faq
        fields = ['question', 'answer', 'department']
        
        