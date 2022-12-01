from django.contrib import admin
from .models import Materials
from .models import Compositions
# Register your models here.

admin.site.register(Materials)
admin.site.register(Compositions)