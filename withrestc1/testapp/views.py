from django.shortcuts import render
from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from testapp.serializers import EmployeeSerializer
from testapp.models import Employee
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
# Create your views here.
class EmployeeCRUDCBV(View):
    #get information
    def get(self,request,*args,**kwarga):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id',None)
        if id is not None:
            emp=Employee.objects.get(id=id)
            serializer=EmployeeSerializer(emp)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        qs=Employee.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        data=JSONParser().parse(stream)
        serializer=EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Resource created successfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        data=JSONParser().parse(stream)
        id=data.get('id')
        emp=Employee.objects.get(id=id)
        #serializer=EmployeeSerializer(emp,data=data)
        serializer = EmployeeSerializer(emp, data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Resource updated successfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data=JSONRenderer().render(serializer.error)
        return HttpResponse(json_data,content_type='application/json')















