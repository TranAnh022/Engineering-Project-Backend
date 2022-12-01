from django.db import models

# Create your models here.

class Materials(models.Model):
        Obj_Id= models.TextField()
        Obj_name=models.TextField()
        elements=models.TextField()
        remarks =models.TextField()
        kg = models.DecimalField(max_digits=6,decimal_places=2)

def __str__(self):
        return self.Obj_Id

class Compositions(models.Model):
        name= models.TextField()
        percentage= models.DecimalField(max_digits=6,decimal_places=2,null=True)
        date= models.DateField(null=True,blank=True)
        price = models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
        material = models.ForeignKey(Materials,on_delete=models.CASCADE,null=True,related_name='modules')

def __str__(self):
        return self.name




