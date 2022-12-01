from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Materials
from django.http import JsonResponse
from .serializers import MaterialSerialzier,CompositionSerialzier
from .models import Materials,Compositions
# Create your views here.

@api_view(['GET'])
def MaterialsAPI(request, pk=0):
       if request.method == 'GET':
              materials = Materials.objects.all()
              materials_serializer = MaterialSerialzier(materials,many=True)
              return JsonResponse(materials_serializer.data,safe=False)
