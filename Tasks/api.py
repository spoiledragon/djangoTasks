from .models import Task
from .serializer import TaskSerializer
from rest_framework import viewsets, permissions

class TasksViewSet(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class=TaskSerializer