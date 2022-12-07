from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import MaterialSerializer,CompositionSerializer
from .models import Materials,Compositions
# Create your views here.

@api_view(['GET'])
def get_material(request, pk=0):
       if request.method == 'GET':
              materials= Materials.objects.all()
              materials_serializer = MaterialSerializer(materials,many=True)
              return JsonResponse(materials_serializer.data,safe=False)
@api_view(['POST'])
def edit_material(request,pk=0):
       if request.method == 'POST':
              composition= Compositions.objects.get(id=request.data["Id"])
              materials= Materials.objects.get(id=8)
              print(materials.modules)
              composition.price= request.data["rates"]
              composition.save()
              composition_serializer= CompositionSerializer(composition)
       return JsonResponse(composition_serializer,safe=False)


class CreateMaterial(APIView):
        def post(self, request, *args, **kwargs):
              material_serializer = Materials.objects.get(id=request.data['Id_mat'])
              serializer = MaterialSerializer(material_serializer,data=request.data)
              if serializer.is_valid():
                     material = serializer.save()
                     serializer = MaterialSerializer(material)
                     return Response(serializer.data, status=status.HTTP_201_CREATED)
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)