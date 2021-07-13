from .emp_serializer import EmployeeSerializer
from rest_framework import viewsets
from .models import Employee

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
