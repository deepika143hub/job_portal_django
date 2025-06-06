from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('job/<int:pk>/apply/', views.apply_for_job, name='apply_for_job'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('my-applications/', views.my_applications, name='my_applications'),

]
