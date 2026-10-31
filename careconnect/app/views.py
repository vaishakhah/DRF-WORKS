from django.shortcuts import render, get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from serializer import DoctorSerializer
from models import Doctor
# Create your views here.
# API VIEWS FOR


class DoctorListCreate(APIView):
    def get(self,request):
        doc = Doctor.objects.all()
        serializers_instance = DoctorSerializer(doc,many=True)
        return Response(serializers_instance.data)


    def post(self,request):
        serializers_instance = DoctorSerializer(data=request.data)
        if serializers_instance.is_valid():
            serializers_instance.save()
            return Response(serializers_instance.data)
        else:
            return Response(serializers_instance.errors)

class DoctorRetrieveUpdateDelete(APIView):
    def get(self,request,pk):
        doc = get_object_or_404(Doctor,pk)
        serializers_instance = DoctorSerializer(doc)
        return Response(serializers_instance.data)

    def put(self,request,pk):
        doc = get_object_or_404(Doctor,pk)
        serializers_instance = DoctorSerializer(instance=doc,data=request.data)
        if serializers_instance.is_valid():
            serializers_instance.save()
            return Response(serializers_instance.data)
        else:
            return Response(serializers_instance.errors)
    def delete(self,request,pk):
        doc = get_object_or_404(Doctor,pk)
        doc.delete()
        return Response({"message":"Deleted Successfully"})







