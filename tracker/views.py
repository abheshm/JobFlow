from django.shortcuts import render
from .models import JobApplication
from .serializers import JobApplicationSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class JobApplicationList(APIView):

    def get(self, request):
        jobs = JobApplication.objects.all()
        serializer = JobApplicationSerializer(jobs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = JobApplicationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class JobApplicationDetail(APIView):

    def get_object(self, pk):
        try:
            return JobApplication.objects.get(pk=pk)
        except JobApplication.DoesNotExist:
            return None
        
    def get(self, request, pk):
        job = self.get_object(pk)
        if not job:
            return Response({'error':'Not found'}, status=404)
        
        serializer = JobApplicationSerializer(job)
        return Response(serializer.data)
    
    def put(self, request, pk):
        job = self.get_object(pk)
        if not job:
            return Response ({'error': 'Not found'}, status=404)
        
        serializer = JobApplicationSerializer(job, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        job = self.get_object(pk)
        if not job:
            return Response({'error': 'Not found'}, status=404)
        
        job.delete()
        return Response({'message': 'Deleted successfully '})

