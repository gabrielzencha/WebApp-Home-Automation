from django.shortcuts import render, HttpResponse
# Create your views here.

def cameraHome (request):
    return render(request, 'cameraHome.html')