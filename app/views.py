from django.shortcuts import render

from django.http import HttpResponse
from app.models import *

# Create your views here.

def insert_topic(request):
    tn=input('Enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic is inserted successfully')

def insert_webpage(request):
    tn=input('enter tn')
    n=input('enter name')
    url=input('enter url')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    WO.save()
    return HttpResponse('Webpage data is inserted')