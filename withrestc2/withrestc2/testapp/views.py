from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.serializers import EmployeeSerializer
from testapp.models import Employee
from rest_framework import generics
# Create your views here.
class EmployeeListAPIView(APIView):
    def get(self,request,format=None):
        qs=Employee.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        return Response(serializer.data)
    '''
    def get(self,request,format=None):
        colors=['RED','BLUE','GREEN','YELLOW','INDIGO']
        return Response({'msg':'welcome to colorful year','colors':colors})
    '''
    '''
    def post(self,request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='Hello{} wish you happy New year!!!'.format(name)
            return Response({'msg':msg})
        return Response(serializer.errors,status=400)

    def put(self,request,pk=None):
        return Response({'msg':'Response from put method'})

    def patch(selfself,request,pk=None):
        return Response({'msg':'Response from patch method'})

    def delete(self,request,pk=None):
        return Response({'msg':'Response from delete method'})
    '''
'''
#to list all employee by using Listapiview
from rest_framework import generics
class EmployeeAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
'''
'''
#how to implement search operation
from rest_framework import generics
class EmployeeAPIView(generics.ListAPIView):
    #queryset=EmployeeSerializer
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        qs=Employee.objects.all()
        name=self.request.GET.get('ename')
        if name is not None:
            qs=qs.filter(ename_icontains=name)
        return qs
'''
'''
#how to implement create opeartion with createapiview
class EmployeeCreateAPIView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
'''
'''
#how to implement retrive operation by using retriveapiview
class EmployeeDeatilAPIView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
'''
'''
#how to implement update operation by using UPDATEAPIVIEW
class EmployeeUpdateAPIView(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'
'''
'''
#how to implement delete operations by using destroyAPIView
class EmployeeDeleteAPIView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'

'''
'''
#how to implement list and create operations by using listcreateAPIView
class EmployeeListCreateAOIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
'''
'''
#how to implement read and update operations by using retriveupadteAPIView
class EmployeeRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
lookup_field='id'
'''
'''
#how to implement read and delete operations by using RetriveDestroyAPIView
class EmployeeRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'

'''
'''
#how to implement read, update, and delete operation by using RetrieveUpdateDestroyAPIView
class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'
'''










