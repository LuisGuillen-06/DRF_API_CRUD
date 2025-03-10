from .models import Project
from rest_framework import viewsets,permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_clases = [permissions.AllowAny]
    serializer_class = ProjectSerializer
    