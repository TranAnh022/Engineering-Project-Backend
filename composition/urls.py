from django.urls import path
from . import views

urlpatterns = [
    path('materials/',views.get_material,name="get_material"),
    path('materials/edit/',views.edit_material)
]
