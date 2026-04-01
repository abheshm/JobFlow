from django.shortcuts import render,redirect
from .models import JobApplication
from .serializers import JobApplicationSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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







def job_list_view(request):
    if request.method=='POST':
        company_name = request.POST.get('company_name')
        job_role = request.POST.get('job_role')
        application_date = request.POST.get('application_date')
        status = request.POST.get('status')
        notes = request.POST.get('notes')

        JobApplication.objects.create(
            company_name=company_name,
            job_role=job_role,
            application_date=application_date,
            status=status,
            notes=notes
        )

        return redirect('job_list')

    jobs = JobApplication.objects.all()
    return render(request, 'job_list.html', {'jobs':jobs})

def delete_job(request,pk):
    jobs = get_object_or_404(JobApplication, pk=pk)
    jobs.delete()
    return redirect('job_list')

def edit_job(request, pk):
    job = get_object_or_404(JobApplication, pk=pk)

    if request.method =='POST':
        job.company_name = request.POST.get('company_name')
        job.job_role = request.POST.get('job_role')
        job.application_date = request.POST.get('application_date')
        job.status = request.POST.get('status')
        job.notes = request.POST.get('notes')
        job.save()
        return redirect('job_list')
    
    return render(request, 'edit_job.html', {"job":job})