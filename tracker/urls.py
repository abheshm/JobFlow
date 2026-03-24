from django.urls import path
from . import views

urlpatterns=[
    path('jobs/',views.JobApplicationList.as_view(),name='job-list'),
    path('jobs/<int:pk>/',views.JobApplicationDetail.as_view(),name='job-detail'),
]