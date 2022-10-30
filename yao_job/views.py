from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
import json

from .models import YaoJob
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        try:
            new_job = YaoJob(
                title=json_data.get('title'),
                description=json_data.get('description'),
                latitude=json_data.get('latitude'),
                longitude=json_data.get('longitude'),
            )
            print(new_job)
            new_job.save()
            return JsonResponse({
                'result': 'success',
            })
        except:
            return HttpResponseBadRequest()
        
    else:
        return JsonResponse(
            {
                'result':
                [{
                    'job_id': j.job_id,
                    'title': j.title,
                    'description': j.description,
                    'latitude': j.latitude,
                    'longitude': j.longitude,
                } for j in YaoJob.objects.all()  ]
                }
            )
    
 
@csrf_exempt
def delete_job(request, job_id):
    if request.method == 'DELETE':
        try:
            retrieve_job = YaoJob.objects.get(job_id=job_id)
            retrieve_job.delete()
            return JsonResponse({
                'result': 'success',
            })
        except:
            return HttpResponseBadRequest()
        
    else:
        return HttpResponseBadRequest()
