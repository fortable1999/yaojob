from django.urls import path

from . import views

app_name = 'yao_jobs'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:job_id>/', views.delete_job, name='delete'),
]
