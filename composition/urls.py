from django.urls import path
from . import views

urlpatterns = [
    path('materials/',views.MaterialsAPI),
    # path('seedAPI/',views.SeedAPI)
]
