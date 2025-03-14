from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','title','description','technology','created_at')
        read_only_fields = ('created_at', )
    
    def validate_title(self, value):
        if Project.objects.filter(title=value).exists():
            raise serializers.ValidationError("Ya existe un proyecto con este titulo.")
        
        return value

