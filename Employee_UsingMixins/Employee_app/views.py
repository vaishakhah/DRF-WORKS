from mypy_django_plugin.transformers import querysets
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from json import loads
# Create your views here.
from django.views import View

from Employee_app import serializer
from Employee_app.models import Employee
from Employee_app.serializer import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins,generics


class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



class EmployeeCreate(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# #apiview for reading a specific employee record
class EmployeeDetail(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#
class EmployeeUpdate(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDelete(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#









