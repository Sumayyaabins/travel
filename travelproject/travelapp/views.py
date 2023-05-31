from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


def demo(request):
    placeobj= Place.objects.all()
    teamobj = Team.objects.all()
    return render(request,"index.html",{'result1':placeobj,'result2':teamobj})