from rest_framework import fields, serializers
from .models import Materials


class MaterialSerialzier(serializers.ModelSerializer):
        class Meta:
                model= Materials
                fields= ('Obj_Id','Obj_name','elements','remarks','kg')