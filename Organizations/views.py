from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Departments
from .serializers import DepartmentSerializer

class DepartmentList(APIView):
    def get(self,request):
        departments = Departments.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class DepartmentDetail(APIView):
    def get(self,request,pk):
        try:
            department = Departments.objects.get(pk=pk)
        except Departments.DoesNotExist:
            return Response({'error': 'Department not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)
    
    def put(self,request,pk):
        department = Departments.objects.get(pk=pk)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    def delete(self,request,pk):
        department = Departments.objects.get(pk=pk)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)