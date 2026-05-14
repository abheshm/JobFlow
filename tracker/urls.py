from django.urls import path
from . import views

urlpatterns=[
    path('jobs/',views.JobApplicationList.as_view(),name='job-list'),
    path('jobs/<int:pk>/',views.JobApplicationDetail.as_view(),name='job-detail'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('register-page/', views.register_page, name='register-page'),
    path('login/', views.LoginView.as_view(), name='login'),

    path('',views.job_list_view, name='job_list'),
    path('delete_job/<int:pk>/',views.delete_job,name='delete_job'),
    path('edit/<int:pk>/',views.edit_job,name='edit_job'),
]