from django.shortcuts import render
from testpp.models import Employee
from testpp.serializers import EmployeeSerializer
from rest_framework import generics
from testpp.pagination import Mypagination
#from testapp.pagination import Mypagination2
#from testapp.pagination import Mypagination2
# Create your views here.
class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = Mypagination
    #pagination_class = Mypagination2
    #pagination_class = Mypagination3



