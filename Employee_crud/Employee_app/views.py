from django.db.models import Q
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from json import loads
# Create your views here.
from django.views import View
from models import Employee
from serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from serializer import EmployeeSerializer

class EmployeeList(APIView):
    def get(self,request):
        #read all employee records from employee table
        emp = Employee.objects.all() #django format qs

        #coverts the qs into python native using employee serializer
        serializer_instance = EmployeeSerializer(emp,many=True) #records more than one

        print(serializer_instance)

        return Response(serializer_instance.data)

class EmployeeCreate(APIView):
    def post(self,request):
        # data = request.data

        #validation + conversion (native to model object)

        serializer_instance = EmployeeSerializer(data=request.data)
        # print(request.data)
        #checks whether the data coming from client is valid,if valid
        #saves the data into model
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        #if data is not valid it will show validation errors

        else:
            return Response(serializer_instance.errors)
#apiview for reading a specific employee record
class EmployeeDetail(APIView):
    def get(self,request,i):
        #reads employee record matching id
        emp= get_object_or_404(Employee,id=i)
        #calls employee serializer class for serialization
        serializer_instance =EmployeeSerializer(emp)
        #sends response back to client
        return Response(serializer_instance.data)



class EmployeeUpdate(APIView):
    def put(self,request,i):


        #reads the records matching with id
        emp =get_object_or_404(Employee,id=i)

        #fetches the data coming from client
        data=request.data

        #calls Employee serializer class for deserialization(validation + conversion)
        serializer_instance=EmployeeSerializer(instance=emp,data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)




class EmployeePartialUpdate(APIView):
    def patch(self,request,i):
        emp = get_object_or_404(Employee, id=i)
        # fetches the data coming from client
        data = request.data

        # calls Employee serializer class for deserialization(validation + conversion)
        serializer_instance = EmployeeSerializer(instance=emp, data=data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)


class SearchEmployee(APIView):
    def get(self,request):
        data = request.query_params.get('search')
        emp = Employee.objects.filter(Q(Name__icontains = data)|Q(Age__icontains=data)|Q(Emp_id__icontains=data)|
                                      Q(Place__icontains=data)|Q(Gender__icontains=data)|Q(Salary__icontains=data)|
                                      Q(Designation__icontains=data))
        serializer_instance = EmployeeSerializer(emp,many=True)
        return Response(serializer_instance.data)



class EmployeeDelete(APIView):
    def delete(self,request,i):
        emp=get_object_or_404(Employee,id=i)
        emp.delete()
        return Response({"message":"Deleted successfully"})


class RegisterUser(APIView):
    def post(self,request):
        serializer_instance = UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)







