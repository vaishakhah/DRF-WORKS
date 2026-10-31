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
from rest_framework import viewsets

class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer









