from django.shortcuts import render
from .models import Faq
from rest_framework.response import Response
from .serializers import FaqSerializer
from rest_framework import status
from rest_framework.views import APIView

class FaqList(APIView):
    def get(self,request):
        faqs = Faq.objects.all()
        serializer = FaqSerializer(faqs,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = FaqSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class FaqDetail(APIView):
    def get(self,request,pk):
        try:
            faq = Faq.objects.get(pk=pk)
        except Faq.DoesNotExist:
            return Response({'error': 'Department not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FaqSerializer(faq)
        return Response(serializer.data)
    
    def put(self,request,pk):
        faq = Faq.objects.get(pk=pk)
        serializer = FaqSerializer(faq, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    def delete(self,request,pk):
        faq = Faq.objects.get(pk=pk)
        faq.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

