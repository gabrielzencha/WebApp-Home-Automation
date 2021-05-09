from django.urls import path
from .views import cameraHome

urlpatterns = [

    path('', cameraHome),
   
]
 