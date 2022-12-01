from rest_framework import fields, serializers
from .models import Materials,Compositions


class CompositionSerialzier(serializers.ModelSerializer):
        class Meta:
                model=Compositions
                fields=('name','percentage')


class MaterialSerialzier(serializers.ModelSerializer):
        modules = CompositionSerialzier(many=True)

        class Meta:
                model= Materials
                fields= ['id','modules']