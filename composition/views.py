from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Materials
from django.http import JsonResponse
from .serializers import MaterialSerialzier
from .models import Compositions
from .models import Materials
# Create your views here.

@api_view(['GET'])
def MaterialsAPI(request, pk=0):
       if request.method == 'GET':
              materials = Materials.objects.all()
              materials_serializer = MaterialSerialzier(materials,many=True)
              return JsonResponse(materials_serializer.data,safe=False)
@api_view(['GET'])
def SeedAPI(request,pk=1):
       if request.method == 'GET':
              material1 =Materials.objects.first()
              composition1= Compositions.objects.create(name="Mn",percentage=10,material=material1)
              composition2= Compositions.objects.create(name="Zn",percentage=15,material=material1)
              material1.composition_set.add(composition1,composition2)
              return Response(material1.composition_set.all())