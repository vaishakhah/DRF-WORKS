from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import title
from django.templatetags.i18n import language
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from MovieAPP import serializer
from MovieAPP.serializer import MovieSerializer
from MovieAPP.models import Movie
from django.db.models import Q
# Create your views here.
from MovieAPP.serializer import UserSerializer
#for reading all records
class Movielist(APIView):
    def get(self,request):
        movie = Movie.objects.all()

        serializer_instance=MovieSerializer(movie,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

# for creating new record
class MovieCreate(APIView):
    def post(self,request):
        serializer_instance = MovieSerializer(data=request.data)
        if serializer_instance.is_valid():

            print(serializer_instance.validated_data)
            director=serializer_instance.validated_data['director']
            print(director)

            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

#for reading one particular record
class MovieDetails(APIView):
    def get(self,request,i):
        movie= get_object_or_404(Movie,id=i)

        serializer_instance=MovieSerializer(movie)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

#for deleting one particular record
class MovieDelete(APIView):
    def delete(self,request,i):
        movie = get_object_or_404(Movie, id=i)
        movie.delete()
        return Response({"message":"Movie Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)

#for updating record
class MovieUpdate(APIView):
    def put(self,request,i):
        data = request.data

        movie = get_object_or_404(Movie,id=i)

        serializer_instance= MovieSerializer(instance=movie,data=data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

#for update specific fields in record
class MovieUpdatePatch(APIView):
    def patch(self,request,i):
        data=request.data

        movie = get_object_or_404(Movie,id=i)

        serializer_instance=MovieSerializer(instance=movie,data=data,partial=True)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


from rest_framework import generics
from rest_framework.filters import SearchFilter


class SearchAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    filter_backends = [SearchFilter]
    search_fields = ['title', 'director', 'runtime', 'rating', 'language','year']

# class RegisterUser(APIView):
#     def post(self,request):
#         serializer_instance = UserSerializer(data=request.data)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data)
#         else:
#             return Response(serializer_instance.errors)
class RegisterAPIView(APIView):
    def post(self,request):
        serializer_instance = UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

# class SearchAPIView(APIView):
#     def get(self,request):
#         data = request.query_params.get('search')
#         print(data)
#         m = Movie.objects.filter(Q(title__icontains=data)|Q(director__icontains = data)|Q(language__icontains = data)|Q(year__icontains=data)|
#         Q(rating__icontains=data)|Q(runtime__icontains =data))
#
#         serializer_instance = MovieSerializer(m,many=True)
#
#         return Response(serializer_instance.data)







