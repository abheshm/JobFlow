from django.urls import path
from . import views

urlpatterns=[
    path('jobs/',views.JobApplicationList.as_view(),name='job-list'),
    path('jobs/<int:pk>/',views.JobApplicationDetail.as_view(),name='job-detail'),

    path('job_list/',views.job_list_view, name='job_list'),
    path('delete_job/<int:pk>/',views.delete_job,name='delete_job'),
]