from rest_framework import fields, serializers
from .models import Materials,Compositions


class CompositionSerializer(serializers.ModelSerializer):
        class Meta:
                model=Compositions
                fields=('name','percentage','id','price')


class MaterialSerializer(serializers.ModelSerializer):
        modules = CompositionSerializer(many=True)

        class Meta:
                model= Materials
                fields= ['id','modules','Obj_name','Obj_Id','remarks','elements','kg']
        def create(self,instance, validated_data):
                print(instance)
                composition_validated_data=validated_data.pop("modules")
                composition_serializer=self.fields['price']
                for each in composition_validated_data:
                        if(each.id == instance.id):
                                each['price']= instance.rates
                compositions = composition_serializer.create(composition_validated_data)
                return compositions

