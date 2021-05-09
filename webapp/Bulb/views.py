from django.shortcuts import render, HttpResponse
# Create your views here.

def bulbHome (request):
    return render(request, 'bulbHome.html')