from django.shortcuts import render
# Create your views here.
from app.models import *
from django.http import HttpResponse




def Display_topic(request):
    LOT=Topic.objects.all()
    D={'LOT':LOT}  
    
    return render(request,'Display_topic.html',D)


def Display_webpage(request):
    LOW=Webpage.objects.all()
    d={'LOW':LOW}
    return render(request,'Display_webpages..html',d)

def Display_AR(request):
    LOA=AccessRecords.objects.all()
    s={'LOA':LOA}
    return render(request,'Display_AR.html',s)