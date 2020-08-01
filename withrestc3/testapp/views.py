from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
class EmployeeCRUDCBV(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

'''
from django.shortcuts import render
from rest_framework.response import Response
from testapp.serializers import NameSerializer
from rest_framework import viewsets
# Create your views here.
class TestViewSet(viewsets.ViewSet):
    def list(selfself,request):
        colors=['RED','GREEN','YELLOW','ORANGE']
        return Response({'msg':'Wish you colorful life in 2020','colors':colors})

    def create(self,request):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='Hello{} your life will be settled in 2020'.format(name)
            return Response({'msg':msg})
        return Response(serializer.errors,status=400)

    def retrieve(self,request,pk=None):
        return Response({'msg':'Response from put method'})

    def update(self,request,pk=None):
        return Response({'msg':'Response from patch method'})

    def partial_update(self,request,pk=None):
        return Response({'msg':'Response from delete method'})

    def destroy(self,request,pk=None):
        return Response({'msg':'Response from destroy method'})
    '''