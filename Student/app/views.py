from django.shortcuts import render, get_object_or_404

# Create your views here.


from app import serializer
from app.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response

from app.serializer import StudentSerializer


# for view
class StudentList(APIView):
    def get(self,request):
        s = Student.objects.all()
        serializer_instance = StudentSerializer(s,many=True)
        print(serializer_instance)
        return Response(serializer_instance.data)

class StudentCreate(APIView):
    def post(self,request):
        serializer_instance = StudentSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class StudentDetails(APIView):
    def get(self,request,i):
        s= get_object_or_404(Student,id=i)
        serializer_instance = StudentSerializer(s)
        return Response(serializer_instance.data)

# # for deleting existing student
class StudentDelete(APIView):
    def delete(self,request,i):
        s=get_object_or_404(Student,id=i)
        s.delete()
        return Response({"message":"DELETED SUCCESSFULLY"})

# #API view for updating(full) existing record
class StudentUpdate(APIView):
    def put(self,request,i):
        s=get_object_or_404(Student,id=i)
        data=request.data
        serializer_instance = StudentSerializer(instance=s,data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)




# #API views for updating(partial) a student record

class StudentPartialUpdate(APIView):
    def patch(self,request,i):
        s= get_object_or_404(Student,id=i)
        data=request.data
        serializer_instance = StudentSerializer(instance=s,data=data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)









