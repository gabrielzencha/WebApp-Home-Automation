from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
def remoteControl(request):
    return render(request, "remoteControlHome.html")